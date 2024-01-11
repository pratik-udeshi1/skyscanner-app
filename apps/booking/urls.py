from django.urls import path

from .views import BookingListView, BookingDetailView

urlpatterns = [
    path('', BookingListView.as_view(), name='booking-list-view'),
    path('<uuid:pk>', BookingDetailView.as_view(), name='booking-detail-view'),
]
