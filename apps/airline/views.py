from django.utils import timezone
from rest_framework import status, filters, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.common.model_utils import *
from .models import Airline
from .serializers import AirlineSerializer
from ..common import permissions, pagination
from ..common.constants import ApplicationMessages


class AirlineListView(generics.ListCreateAPIView):
    model = Airline
    serializer_class = AirlineSerializer
    permission_classes = [IsAuthenticated, permissions.IsStaff]
    pagination_class = pagination.DefaultPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'code']
    ordering = ['-created_at']

    def get_queryset(self):
        return filter_instance(self.model)

    def get(self, request, *args, **kwargs):
        filtered_qs = self.filter_queryset(self.get_queryset())
        serializer = self.serializer_class(self.paginate_queryset(filtered_qs), many=True, context={'is_get': True})
        return Response(data=self.get_paginated_response(serializer.data).data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'is_post': True})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AirlineDetailView(APIView):
    model = Airline
    serializer_class = AirlineSerializer
    permission_classes = [IsAuthenticated, permissions.IsStaff]
    pagination_class = pagination.DefaultPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'code']
    ordering = ['-created_at']

    def get_queryset(self, pk):
        qs_filters = {'pk': pk}
        return get_object_or_notfound(self.model, **qs_filters)

    def get(self, request, pk):
        filtered_qs = self.get_queryset(pk=pk)
        serializer = self.serializer_class(filtered_qs)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        airline = self.get_queryset(pk)
        serializer = AirlineSerializer(airline, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        airline = get_object_or_notfound(self.model, pk=pk)
        airline.deleted_at = timezone.now()
        airline.save()
        return Response(ApplicationMessages.RECORD_DELETED, status=status.HTTP_204_NO_CONTENT)
