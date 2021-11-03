import graphene
import json
from tornado_graphql_api.types import Planets, Planet
from pprint import pprint
from tornado.httpclient import AsyncHTTPClient

SWAPI_URL = 'https://swapi.dev/api'


class QueryPlanet(graphene.ObjectType):
    planet = graphene.Field(Planet)
    planets = graphene.Field(Planets)

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

    async def resolve_planets(self, info):
        http_client = AsyncHTTPClient()
        response = await http_client.fetch(f'{SWAPI_URL}/planets')
        print('Info: ', info)
        pprint(json.loads(response.body))
        planets = json.loads(response.body)
        return Planets(count=planets.get('count'),
                       next=planets.get('next'),
                       previous=planets.get('previous'),
                       results=planets.get('results'))

