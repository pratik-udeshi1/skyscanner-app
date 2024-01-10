from django.urls import path

from .views import AirlineListView, AirlineDetailView

urlpatterns = [
    path('', AirlineListView.as_view(), name='airline-list-view'),
    path('<uuid:pk>', AirlineDetailView.as_view(), name='airline-detail-view'),
]
