# vehicle/views.py
from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from account.models import User  # Adjust the import based on your project structure
from .models import Vehicle,History
from .serializers import VehicleSerializer,VehicleHistorySerializer

class VehicleListCreateView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleHistoryCreateView(generics.CreateAPIView):
    queryset = History.objects.all()
    serializer_class = VehicleHistorySerializer

    def perform_create(self, serializer):
        # Add your conditions before creating the object
        vehicle_id = self.request.data.get('vehicle')
        check_online = len(History.objects.filter(vehicle=Vehicle.objects.get(id=vehicle_id),completed = False))
        if check_online == 0:
            # Your custom logic here
            serializer.save()
        else:
            # Handle the case where the condition is not met
            raise serializers.ValidationError({"error": "You have already checked-in please checkout"})
