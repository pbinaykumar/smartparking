# vehicle/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from account.models import User  # Adjust the import based on your project structure
from .models import Vehicle
from .serializers import VehicleSerializer

class VehicleListCreateView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    # def perform_create(self, serializer):
    #     print("self.request")
    #     serializer.save(user=User.objects.get(self.request.data['user']))

class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

# def vehicle_status(request):
#     queryset = Vehicle.objects.all()
