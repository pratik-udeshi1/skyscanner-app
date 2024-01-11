from django.urls import path

from .views import AirportListView, AirportDetailView

urlpatterns = [
    path('', AirportListView.as_view(), name='airport-list-view'),
    path('<uuid:pk>', AirportDetailView.as_view(), name='airport-detail-view'),
]
