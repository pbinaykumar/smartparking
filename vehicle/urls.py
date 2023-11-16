# vehicle/urls.py
from django.urls import path
from .views import VehicleListCreateView, VehicleDetailView, MyView

urlpatterns = [
    path('vehicles/', VehicleListCreateView.as_view(), name='vehicle-list-create'),
    path('vehicles/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('check-token/', MyView.as_view()),
]
