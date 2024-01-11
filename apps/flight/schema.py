import graphene
from graphene_django.types import DjangoObjectType

from .models import Flight


class FlightType(DjangoObjectType):
    class Meta:
        model = Flight

    airline = graphene.Field('apps.airline.schema.AirlineType')
    departure_airport = graphene.Field('apps.airport.schema.AirportType')
    arrival_airport = graphene.Field('apps.airport.schema.AirportType')


class Query(graphene.ObjectType):
    flights = graphene.List(FlightType)

    def resolve_flights(self, info):
        return Flight.objects.all()


schema = graphene.Schema(query=Query)
