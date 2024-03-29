from django.contrib import admin
from django.urls import include
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from graphene_django.views import GraphQLView
from rest_framework import permissions

from apps.flight.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('apps.user.urls')),
    path('api/v1/airline/', include('apps.airline.urls')),
    path('api/v1/airport/', include('apps.airport.urls')),
    path('api/v1/flight/', include('apps.flight.urls')),
    path('api/v1/booking/', include('apps.booking.urls')),
    path('api/v1/graphql/', GraphQLView.as_view(graphiql=True, schema=schema), name='graphql'),

]

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns += [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
