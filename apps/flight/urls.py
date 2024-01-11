from django.urls import path

from .views import FlightListView, FlightDetailView

urlpatterns = [
    path('', FlightListView.as_view(), name='flight-list-view'),
    path('<uuid:pk>', FlightDetailView.as_view(), name='flight-detail-view'),
]
