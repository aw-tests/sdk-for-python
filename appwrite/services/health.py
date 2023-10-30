from ..service import Service
from ..exception import AppwriteException

class Health(Service):

    def __init__(self, client):
        super(Health, self).__init__(client)

    def get(self):
        """Get HTTP"""

        
        api_path = '/health'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_antivirus(self):
        """Get antivirus"""

        
        api_path = '/health/anti-virus'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_cache(self):
        """Get cache"""

        
        api_path = '/health/cache'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_db(self):
        """Get DB"""

        
        api_path = '/health/db'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_pub_sub(self):
        """Get pubsub"""

        
        api_path = '/health/pubsub'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue(self):
        """Get queue"""

        
        api_path = '/health/queue'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_builds(self):
        """Get builds queue"""

        
        api_path = '/health/queue/builds'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_certificates(self):
        """Get certificates queue"""

        
        api_path = '/health/queue/certificates'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_databases(self, name = None):
        """Get databases queue"""

        
        api_path = '/health/queue/databases'
        api_params = {}

        api_params['name'] = name

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_deletes(self):
        """Get deletes queue"""

        
        api_path = '/health/queue/deletes'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_functions(self):
        """Get functions queue"""

        
        api_path = '/health/queue/functions'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_logs(self):
        """Get logs queue"""

        
        api_path = '/health/queue/logs'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_mails(self):
        """Get mails queue"""

        
        api_path = '/health/queue/mails'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_messaging(self):
        """Get messaging queue"""

        
        api_path = '/health/queue/messaging'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_migrations(self):
        """Get migrations queue"""

        
        api_path = '/health/queue/migrations'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_webhooks(self):
        """Get webhooks queue"""

        
        api_path = '/health/queue/webhooks'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_storage_local(self):
        """Get local storage"""

        
        api_path = '/health/storage/local'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_time(self):
        """Get time"""

        
        api_path = '/health/time'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)
