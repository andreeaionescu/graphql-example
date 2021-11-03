# graphql-example

Two working examples on how graphql and graphene work with either Flask or Tornado.

1. GraphQL, Graphene, Flask and SQL Alchemy.
A Flask server has been used to expose the GraphQL schema under /graphql endpoint.
The picture below queries for all employees within an organization and it is displayed via the interface GraphiQL.

![image](https://user-images.githubusercontent.com/12115225/139962858-15c07d72-3bfb-4588-bc82-56e9fb9b8631.png)

This example was taken from the official tutorial https://docs.graphene-python.org/projects/sqlalchemy/en/latest/tutorial/.

2. GraphQL, Graphene-Tornado and Star Wars API (https://swapi.dev/).
Graphene-tornado library has been used to expose the schema using a custom tornado request handler and async resolvers.
The picture below queries for planets from the Star Wars API.

![image](https://user-images.githubusercontent.com/12115225/139970335-eceefc77-db4e-4888-a8a4-86cea3e39d43.png)

More details on Graphene-tornado at the repo https://github.com/graphql-python/graphene-tornado, 
