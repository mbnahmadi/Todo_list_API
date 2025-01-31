from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
# from .models import User


User = get_user_model()

class registerUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['name' , 'email' , 'password']

    def create(self,validate_data):
        user = User.objects.create_user(
            email = validate_data['email'],
            name = validate_data['name'],
            password = validate_data['password']
        )
        return user

        # refresh = RefreshToken.for_user(user)

        # return {
        #     "user": user,
        #     "refresh": str(refresh),
        #     "access": str(refresh.access_token)
        # }
