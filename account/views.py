# account/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth.hashers import make_password

class SignUpView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Ensure that a password is provided
        password = self.request.data.get('password')
        if not password:
            return Response({'error': 'Password is required'}, status=400)

        # Hash the password before saving the user
        user = serializer.save(password=make_password(password))

        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response(data, status=201)

class SignInView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = CustomUser.objects.get(email=email)

        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(data)
        else:
            return Response({'error': 'Invalid credentials'}, status=400)
