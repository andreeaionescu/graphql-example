import graphene


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


class Planets(graphene.ObjectType):
    count = graphene.Int()
    next = graphene.String()
    previous = graphene.String()
    results = graphene.List(Planet)
