# vehicle/urls.py
from django.urls import path
from .views import VehicleListCreateView, VehicleDetailView, VehicleHistoryCreateView,parking_bill, vehicle_checkout

urlpatterns = [
    path('vehicles/', VehicleListCreateView.as_view(), name='vehicle-list-create'),
    path('vehicle/<int:pk>/', VehicleDetailView.as_view(), name='vehicle detail'),
    path('checkin/', VehicleHistoryCreateView.as_view(), name='vehicle checkin'),
    path('parking-bill/', parking_bill, name='parking bill'),
    path('checkout/', vehicle_checkout, name='vehicle checkout'),
]
