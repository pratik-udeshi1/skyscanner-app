import graphene
from graphene_django.types import DjangoObjectType

from .models import Airport


class AirportType(DjangoObjectType):
    class Meta:
        model = Airport

    flights = graphene.List('apps.flight.schema.FlightType')
    airlines = graphene.List('apps.airline.schema.AirlineType')


class Query(graphene.ObjectType):
    airports = graphene.List(AirportType)

    def resolve_airports(self, info):
        return Airport.objects.all()


schema = graphene.Schema(query=Query)
