import tornado.web
import graphene
from tornado.ioloop import IOLoop

from graphene_tornado.schema import schema
from graphene_tornado.tornado_graphql_handler import TornadoGraphQLHandler
from tornado_graphql_api.queries import QueryPlanet


class ExampleApplication(tornado.web.Application):

    def __init__(self):
        schema_planet = graphene.Schema(query=QueryPlanet)
        handlers = [
            (r'/graphql', TornadoGraphQLHandler, dict(graphiql=True, schema=schema)),
            (r'/graphql/planets', TornadoGraphQLHandler, dict(graphiql=True, schema=schema_planet))
        ]
        tornado.web.Application.__init__(self, handlers)


if __name__ == '__main__':
    app = ExampleApplication()
    app.listen(1111)
    print('OK')
    IOLoop.instance().start()
