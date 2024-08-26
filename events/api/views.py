from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response

from .serializers import UserSerializer, EventSerializer, RsvpSerializer, CommentSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Event, Rsvp, Comment

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({ 'detail': "Not found"}, status=status.HTTP_404_NOT_FOUND )
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"Token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"Token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def rsvp(request):
    if request.method == 'GET':
        user = request.user.id
        rsvps = Rsvp.objects.filter(user=user)
        serializer = RsvpSerializer(rsvps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data
        event = get_object_or_404(Event, id=request.data['event'])
        rsvp_exist = Rsvp.objects.filter(user=request.user, event=event)
        if rsvp_exist:
            return Response({ 'detail': "Already RSVP'd to event"}, status=status.HTTP_400_BAD_REQUEST )
        data['user'] = request.user.id
        data['event'] = event.id
        serializer = RsvpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({ 'detail': "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED )


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def rsvp_detail(request, pk):
    rsvp = get_object_or_404(Rsvp, id=pk)
    if rsvp.user != request.user:
        return Response({ 'detail': "Not authorized"}, status=status.HTTP_401_UNAUTHORIZED )
    if request.method == 'GET':
        serializer = RsvpSerializer(rsvp)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = request.data
        data['user'] = request.user.id
        data['event'] = rsvp.event.id
        serializer = RsvpSerializer(rsvp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        rsvp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({ 'detail': "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def post_comment(request):
    pk = request.data['event']
    data = request.data
    event = get_object_or_404(Event, id=pk)
    data['user'] = request.user.id
    data['event'] = event.id
    serializer = CommentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def get_comments(request, pk):
    event = get_object_or_404(Event, id=pk)
    comments = Comment.objects.filter(event=event)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def user_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    if comment.user != request.user:
        return Response({ 'detail': "Not authorized"}, status=status.HTTP_401_UNAUTHORIZED )
    if request.method == 'PUT':
        data = request.data
        data['user'] = request.user.id
        data['event'] = comment.event.id
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({ 'detail': "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED )
