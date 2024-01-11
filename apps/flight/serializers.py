from datetime import datetime
from decimal import Decimal

from rest_framework import serializers

from .models import Flight
from ..airline.serializers import AirlineSerializer
from ..airport.serializers import AirportSerializer
from ..common.exclude_fields import ExcludeFieldsMixin


class FlightSerializer(ExcludeFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def validate(self, data):
        if data['price'] < 1 and Decimal(data['price']):
            raise serializers.ValidationError(f"Price should be Positive and a number")

        if 'departure_time' in data and data['departure_time'] > data['arrival_time']:
            raise serializers.ValidationError(f"Departure time should not be Greater than Arrival")
        return data

    def create(self, validated_data):
        flight_instance = Flight.objects.create(**validated_data)
        return flight_instance

    def get_airline_obj(self, instance):
        return AirlineSerializer(instance.airline).data if instance.airline else None

    def get_d_airport_obj(self, instance):
        return AirportSerializer(instance.departure_airport).data if instance.departure_airport else None

    def get_a_airport_obj(self, instance):
        return AirportSerializer(instance.arrival_airport).data if instance.arrival_airport else None

    def get_flight_duration(self, representation):
        departure_time = representation['departure_time']
        arrival_time = representation['arrival_time']
        start_time = datetime.strptime(departure_time, '%Y-%m-%dT%H:%M:%SZ')
        end_time = datetime.strptime(arrival_time, '%Y-%m-%dT%H:%M:%SZ')
        duration_in_seconds = (end_time - start_time).total_seconds()
        duration_in_hours = duration_in_seconds / 3600
        return duration_in_hours

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['airline'] = self.get_airline_obj(instance)
        representation['departure_airport'] = self.get_d_airport_obj(instance)
        representation['arrival_airport'] = self.get_a_airport_obj(instance)
        representation['flight_duration'] = self.get_flight_duration(representation)
        return representation
