# vehicle/urls.py
from django.urls import path
from .views import VehicleListCreateView, VehicleDetailView

urlpatterns = [
    path('vehicles/', VehicleListCreateView.as_view(), name='vehicle-list-create'),
    path('vehicle/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('status/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
]
