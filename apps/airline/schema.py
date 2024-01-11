import graphene
from graphene_django.types import DjangoObjectType

from .models import Airline


class AirlineType(DjangoObjectType):
    class Meta:
        model = Airline

    flights = graphene.List('apps.flight.schema.FlightType')
    departure_airport = graphene.Field('apps.airport.schema.AirportType')
    arrival_airport = graphene.Field('apps.airport.schema.AirportType')


class Query(graphene.ObjectType):
    airlines = graphene.List(AirlineType)

    def resolve_airlines(self, info):
        return Airline.objects.all()


schema = graphene.Schema(query=Query)
