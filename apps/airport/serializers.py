from rest_framework import serializers, validators

from .models import Airport
#
# class AirportSerializer(ExcludeFieldsMixin, serializers.ModelSerializer):
#     test_1 = serializers.CharField(write_only=True, required=False)
#     test_2 = serializers.CharField(write_only=True, required=False)
#
#     code = serializers.CharField(validators=[validators.UniqueValidator(
#         queryset=Airport.objects.all(),
#         message='Code already exists, please submit a unique one.')])
#
#     class Meta:
#         model = Airport
#         fields = '__all__'
#
#     def validate(self, data):
#         max_limit = 3
#         if data.get('code') and len(data.get('code')) > max_limit:
#             raise serializers.ValidationError(f"Code cannot be more than {max_limit} characters.")
#
#         if data.get('name') and not all(x.isalnum() or x.isspace() for x in data.get('name', None)):
#             raise serializers.ValidationError("Flight name cannot contain special characters.")
#
#         return data
#
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         if self.context.get('is_get') or self.context.get('is_post'):
#             representation['name'] = representation['name'].upper()
#             test_data = self.context.get('test_data')
#             if test_data:
#                 representation.update(test_data)
#         return representation
#
#     def create(self, validated_data):
#         test_data = {
#             'test_1': validated_data.pop('test_1', None),
#             'test_2': validated_data.pop('test_2', None),
#         }
#         self.context['test_data'] = test_data
#         return Airport.objects.create(**validated_data)
from ..common.exclude_fields import ExcludeFieldsMixin


class AirportGetSerializer(serializers.ModelSerializer):
    test_1 = serializers.CharField(write_only=True, required=False)
    test_2 = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Airport
        fields = ['test_1', 'test_2', ]


class AirportSerializer(ExcludeFieldsMixin, serializers.ModelSerializer):
    test_1 = serializers.CharField(write_only=True, required=False)
    test_2 = serializers.CharField(write_only=True, required=False)

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

    def to_representation(self, instance):
        representation = super().to_representation(instance['airport'])
        if self.context.get('is_get') or self.context.get('is_post'):
            representation['name'] = representation['name'].upper()
            test_data = instance['test_data'].instance
            if test_data:
                representation.update(test_data)
        return representation

    def create(self, validated_data):
        print("validated_data", validated_data)
        test_data = {
            'test_1': validated_data.pop('test_1', None),
            'test_2': validated_data.pop('test_2', None),
        }
        airport_instance = Airport.objects.create(**validated_data)
        test_data_serializer = AirportGetSerializer(test_data)
        representation = {
            'airport': airport_instance,
            'test_data': test_data_serializer
        }
        return representation
