from rest_framework import serializers, validators

from .models import Airport
from ..common.exclude_fields import ExcludeFieldsMixin


class AirportGetSerializer(serializers.Serializer):
    test_1 = serializers.CharField()
    test_2 = serializers.CharField()


class AirportSerializer(ExcludeFieldsMixin, serializers.ModelSerializer):
    test_data = AirportGetSerializer(write_only=True, required=False)

    code = serializers.CharField(validators=[validators.UniqueValidator(
        queryset=Airport.objects.all(),
        message='Code already exists, please submit a unique one.')])

    class Meta:
        model = Airport
        fields = '__all__'

    def validate(self, data):
        max_limit = 3
        if data.get('code') and len(data.get('code')) > max_limit:
            raise serializers.ValidationError(f"Code cannot be more than {max_limit} characters.")

        if data.get('name') and not all(x.isalnum() or x.isspace() for x in data.get('name', None)):
            raise serializers.ValidationError("Flight name cannot contain special characters.")

        return data

    def create(self, validated_data):
        test_data = validated_data.pop('test_data', None)
        test_data_serializer = AirportGetSerializer(test_data)

        airport_instance = Airport.objects.create(**validated_data)
        airport_instance.test_data = test_data_serializer
        return airport_instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if 'name_upper' in self.context:
            representation['name'] = representation['name'].upper()
        if hasattr(instance, 'test_data'):
            test_data = instance.test_data.instance
            representation.update({"test_data": test_data})
        return representation
