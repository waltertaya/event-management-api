from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from .models import UserProfile
from .serializers import UserSerializer

from django.contrib.auth.models import User

class RegisterAPIView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user_data = {
            'username': request.data.get('username'),
            'password': request.data.get('password'),
            'email': request.data.get('email'),
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name')
        }
        user = User.objects.create_user(
            username=user_data['username'],
            password=user_data['password'],
            email=user_data['email'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name']
        )
        mutable_data = request.data.copy()
        mutable_data['user'] = user.id
        serializer = self.get_serializer(data=mutable_data)
        if serializer.is_valid():
            user_profile = serializer.save(user=user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "message": "User registered successfully!",
                "user": serializer.data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        try:
            user_profile = UserProfile.objects.get(username=username)

            if check_password(password, user_profile.password):
                token, created = Token.objects.get_or_create(user=user_profile.user)
                user_data = UserSerializer(user_profile).data
                return Response({
                    "message": "Login successful!",
                    "user": user_data,
                    "token": token.key
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid password."}, status=status.HTTP_400_BAD_REQUEST)
        except UserProfile.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

