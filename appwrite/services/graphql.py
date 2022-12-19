from ..service import Service
from ..exception import AppwriteException

class Graphql(Service):

    def __init__(self, client):
        super(Graphql, self).__init__(client)

    def a0228ea55af(self, query, operation_name = None, variables = None):
        """GraphQL Endpoint"""

        
        path = '/graphql'
        params = {}
        if query is None:
            raise AppwriteException('Missing required parameter: "query"')


        params['query'] = query
        params['operationName'] = operation_name
        params['variables'] = variables

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def query(self, query):
        """GraphQL Endpoint"""

        
        path = '/graphql'
        params = {}
        if query is None:
            raise AppwriteException('Missing required parameter: "query"')


        params['query'] = query

        return self.client.call('post', path, {
            'x-sdk-graphql': 'true',
            'content-type': 'application/json',
        }, params)

    def mutation(self, query):
        """GraphQL Endpoint"""

        
        path = '/graphql/mutation'
        params = {}
        if query is None:
            raise AppwriteException('Missing required parameter: "query"')


        params['query'] = query

        return self.client.call('post', path, {
            'x-sdk-graphql': 'true',
            'content-type': 'application/json',
        }, params)
