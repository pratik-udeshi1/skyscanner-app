from rest_framework import serializers, validators

from .models import Airline
from ..common.exclude_fields import ExcludeFieldsMixin


class AirlineSerializer(ExcludeFieldsMixin, serializers.ModelSerializer):
    code = serializers.CharField(validators=[validators.UniqueValidator(
        queryset=Airline.objects.all(),
        message='Code already exists, please submit a unique one.')])

    class Meta:
        model = Airline
        fields = '__all__'

    def validate(self, data):
        max_limit = 5
        if data.get('code') and len(data.get('code')) > max_limit:
            raise serializers.ValidationError(f"Code cannot be more than {max_limit} characters.")

        if data.get('name') and not all(x.isalnum() or x.isspace() for x in data.get('name', None)):
            raise serializers.ValidationError("Flight name cannot contain special characters.")

        return data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get('is_get') or self.context.get('is_post'):
            representation['name'] = representation['name'].upper()
        return representation
