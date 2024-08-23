from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'email',
            'first_name',
            'last_name',
            'username',
            'password'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = validated_data.pop('user')
        user_profile = UserProfile.objects.create(user=user, **validated_data)
        return user_profile
