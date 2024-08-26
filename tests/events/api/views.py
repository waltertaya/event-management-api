from rest_framework import generics
from .models import RSVP, Comment
from .serializers import RSVPSerializer, CommentSerializer


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class RSVPAPIView(generics.CreateAPIView):
    queryset = RSVP.objects.all()
    serializer_class = RSVPSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = []


class CommentAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = []

