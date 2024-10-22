from rest_framework import serializers
from .models import User


class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name' , 'email' , 'password']

    def create(self,validate_data):
        user = User(
            name = validate_data['name'],
            email = validate_data['email']
        )
        user.set_password(validate_data['password'])
        user.save()
        return user
