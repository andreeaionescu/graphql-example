import tornado.web
import json
import graphene
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient

from graphene_tornado.schema import schema
from graphene_tornado.tornado_graphql_handler import TornadoGraphQLHandler

SWAPI_URL = 'https://swapi.dev/api'


class Planet(graphene.ObjectType):
    name = graphene.String()
    rotation_period = graphene.String()
    orbital_period = graphene.String()
    diameter = graphene.String()
    climate = graphene.String()
    gravity = graphene.String()
    terrain = graphene.String()
    surface_water = graphene.String()
    population = graphene.String()
    residents = graphene.List(graphene.String)
    films = graphene.List(graphene.String)
    created = graphene.String()
    edited = graphene.String()
    url = graphene.String()


class QueryPlanet(graphene.ObjectType):
    planet = graphene.Field(Planet)

    async def resolve_planet(self, info):
        http_client = AsyncHTTPClient()
        response = await http_client.fetch(f'{SWAPI_URL}/planets/1')
        print('Info: ', info)
        print(json.loads(response.body))
        planet = json.loads(response.body)
        return Planet(name=planet.get('name'),
                      rotation_period=planet.get('rotation_period'),
                      orbital_period=planet.get('orbital_period'),
                      diameter=planet.get('diameter'),
                      climate=planet.get('climate'),
                      gravity=planet.get('gravity'),
                      terrain=planet.get('terrain'),
                      surface_water=planet.get('surface_water'),
                      population=planet.get('population'),
                      residents=planet.get('residents'),
                      films=planet.get('films'),
                      created=planet.get('created'),
                      edited=planet.get('edited'),
                      url=planet.get('url'),
                      )


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
