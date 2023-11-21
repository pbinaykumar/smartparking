# vehicle/views.py
from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from account.models import User  # Adjust the import based on your project structure
from .models import Vehicle,History
from .serializers import VehicleSerializer,VehicleHistorySerializer
from rest_framework import status

class VehicleListCreateView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response = {
                'success': True,
                'status_code': status.HTTP_201_CREATED,
                'message': "Vehicle created successfully."
            }
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            response = {
                'success': False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': list(serializer.errors.items())[0][1][0]
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer



class VehicleHistoryCreateView(generics.CreateAPIView):
    queryset = History.objects.all()
    serializer_class = VehicleHistorySerializer

    def create(self, request, *args, **kwargs):
        # Add your conditions before creating the object
        vehicle_id = request.data.get('vehicle')
        check_online = len(History.objects.filter(vehicle=Vehicle.objects.get(id=vehicle_id),completed = False))
        if check_online == 0:
            # Your custom logic here
            serializer =  VehicleHistorySerializer(data = request.data)
            if not serializer.is_valid():
                status_code = status.HTTP_400_BAD_REQUEST
                response = {
                    'success': False,
                    'status code': status_code,
                    'message': list(serializer.errors.items())[0][1][0]
                }
            else:
                response = {
                    'success': True,
                    'status_code': status.HTTP_200_OK,
                    'message': "Successful check-in."
                }
            return Response(response, status=status.HTTP_200_OK)
        else:
            # Handle the case where the condition is not met
            response = {
                'success': False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': "You have already checked-in please checkout"
            }
            raise serializers.ValidationError(response)
