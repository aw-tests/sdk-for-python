import io
import requests
import os
from .input_file import InputFile
from .exception import AppwriteException

class Client:
    def __init__(self):
        self._chunk_size = 5*1024*1024
        self._self_signed = False
        self._endpoint = 'https://HOSTNAME/v1'
        self._global_headers = {
            'content-type': '',
            'x-sdk-version': 'appwrite:python:0.6.0',
            'X-Appwrite-Response-Format' : '0.12.0',
        }

    def set_self_signed(self, status=True):
        self._self_signed = status
        return self

    def set_endpoint(self, endpoint):
        self._endpoint = endpoint
        return self

    def add_header(self, key, value):
        self._global_headers[key.lower()] = value
        return self

    def set_project(self, value):
        """Your project ID"""

        self._global_headers['x-appwrite-project'] = value
        return self

    def set_key(self, value):
        """Your secret API key"""

        self._global_headers['x-appwrite-key'] = value
        return self

    def set_jwt(self, value):
        """Your secret JSON Web Token"""

        self._global_headers['x-appwrite-jwt'] = value
        return self

    def set_locale(self, value):
        self._global_headers['x-appwrite-locale'] = value
        return self

    def call(self, method, path='', headers=None, params=None):
        if headers is None:
            headers = {}

        if params is None:
            params = {}

        data = {}
        json = {}
        files = {}
        
        headers = {**self._global_headers, **headers}

        if method != 'get':
            data = params
            params = {}

        if headers['content-type'].startswith('application/json'):
            json = data
            data = {}

        if headers['content-type'].startswith('multipart/form-data'):
            del headers['content-type']
            
            for key in data.copy():
                if isinstance(data[key], InputFile):
                    files[key] = (data[key].name, data[key].file)
                    del data[key]
        response = None
        try:
            response = requests.request(  # call method dynamically https://stackoverflow.com/a/4246075/2299554
                method=method,
                url=self._endpoint + path,
                params=self.flatten(params),
                data=self.flatten(data),
                json=json,
                files=files,
                headers=headers,
                verify=(not self._self_signed),
            )

            response.raise_for_status()

            content_type = response.headers['Content-Type']

            if content_type.startswith('application/json'):
                return response.json()

            return response._content
        except Exception as e:
            if response != None:
                content_type = response.headers['Content-Type']
                if content_type.startswith('application/json'):
                    raise AppwriteException(response.json()['message'], response.status_code, response.json().get('type'), response.json())
                else:
                    raise AppwriteException(response.text, response.status_code)
            else:
                raise AppwriteException(e)

    def chunked_upload(
        self,
        path,
        headers = None,
        params = None,
        param_name = '',
        on_progress = None,
    ):
        file_path = str(params[param_name])
        file_name = os.path.basename(file_path)
        size = os.stat(file_path).st_size

        if size < self._chunk_size:
            slice = open(file_path, 'rb').read()
            params[param_name] = InputFile(file_path, file_name, slice)
            return self.call(
                'post',
                path,
                headers,
                params
            )

        input = open(file_path, 'rb')
        offset = 0

        while offset < size:
            slice = input.read(self._chunk_size) or input.read(size - offset)

            params[param_name] = InputFile(file_path, file_name, slice)
            headers["content-range"] = f'bytes {offset}-{min((offset + self._chunk_size) - 1, size)}/{size}'

            result = self.call(
                'post',
                path,
                headers,
                params,
            )
            
            offset = offset + self._chunk_size
            
            if "$id" in result: 
                headers["x-appwrite-id"] = result["$id"]

            if on_progress is not None:
                on_progress({
                    "$id": result["$id"],
                    "progress": min(offset, size)/size * 100,
                    "sizeUploaded": end+1,
                    "chunksTotal": result["chunksTotal"],
                    "chunksUploaded": result["chunksUploaded"],
                })

        return result

    def flatten(self, data, prefix=''):
        output = {}
        i = 0

        for key in data:
            value = data[key] if isinstance(data, dict) else key
            finalKey = prefix + '[' + key +']' if prefix else key
            finalKey = prefix + '[' + str(i) +']' if isinstance(data, list) else finalKey
            i += 1
            
            if isinstance(value, list) or isinstance(value, dict):
                output = {**output, **self.flatten(value, finalKey)}
            else:
                output[finalKey] = value

        return output

