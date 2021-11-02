'''
Unlike a RESTful API, there is only a single URL from which GraphQL is accessed.

We are going to use Flask to create a server that expose the GraphQL schema under /graphql and a interface for querying
it easily: GraphiQL (also under /graphql when accessed by a browser).
'''
from flask import Flask
from flask_graphql import GraphQLView

from flask_sqlalchemy.models import db_session
from flask_sqlalchemy.schema import schema, Department

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()