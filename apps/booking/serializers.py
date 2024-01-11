from decimal import Decimal

from rest_framework import serializers

from .models import Booking
from ..common.exclude_fields import ExcludeFieldsMixin
from ..flight.serializers import FlightSerializer


class BookingSerializer(ExcludeFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Booking
        exclude = ['user']

    def validate(self, data):
        if 'total_price' in data and data['total_price'] < 1 and Decimal(data['total_price']):
            raise serializers.ValidationError(f"Price should be Positive and a number")

        if 'departure_date' in data and data['departure_date'] > data['return_date']:
            raise serializers.ValidationError(f"Departure date should not be Greater than Return")
        return data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        booking_instance = Booking.objects.create(**validated_data)
        return booking_instance

    def get_flight_obj(self, instance):
        return FlightSerializer(instance.flight).data if instance.flight else None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['flight'] = self.get_flight_obj(instance)
        return representation
