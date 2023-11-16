# vehicle/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from account.models import CustomUser  # Adjust the import based on your project structure
from .models import Vehicle
from .serializers import VehicleSerializer

class VehicleListCreateView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]


from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class MyView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        print("request.headers==")
        print(request.headers)
        # Check if the access token is present in the request headers
        if 'Authorization' not in request.headers:
            return Response({'detail': 'Authentication credentials were not provided.'},
                            status=status.HTTP_401_UNAUTHORIZED)

        # Extract the access token from the Authorization header
        auth_header = request.headers['Authorization']
        _, token = auth_header.split(' ')

        # Now you have the token, and you can perform any additional checks or use it as needed
        # For example, you can print it or check its validity against your authentication system
        print(f'Token: {token}')

        return Response({'detail': 'Success!'}, status=status.HTTP_200_OK)
