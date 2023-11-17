# vehicle/urls.py
from django.urls import path
from .views import VehicleListCreateView, VehicleDetailView, VehicleHistoryCreateView

urlpatterns = [
    path('vehicles/', VehicleListCreateView.as_view(), name='vehicle-list-create'),
    path('vehicle/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('check-in/', VehicleHistoryCreateView.as_view(), name='vehicle-check-in'),
]
