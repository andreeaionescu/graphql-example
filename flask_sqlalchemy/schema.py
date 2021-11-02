'''
GraphQL presents your objects to the world as a graph structure rather than a more hierarchical structure
to which you may be accustomed. In order to create this representation, Graphene needs to know about each type of object
which will appear in the graph.

This graph also has a root type through which all access begins.
This is the Query class below.
In this example, we provide the ability to list all employees via all_employees,
and the ability to obtain a specific node via node.
'''
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_sqlalchemy.models import db_session, Department as DepartmentModel, Employee as EmployeeModel


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_employees = SQLAlchemyConnectionField(Employee.connection)
    # Disable sorting over this field
    all_departments = SQLAlchemyConnectionField(Department.connection, sort=None)


schema = graphene.Schema(query=Query)
