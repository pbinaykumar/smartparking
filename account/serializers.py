from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserSigninSerializer(serializers.Serializer):
    user_id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'Please check the email id and password again !'
            )
        return user

    def get_user_id(self,obj):
        return obj.user_id
    def get_name(self,obj):
        return obj.name