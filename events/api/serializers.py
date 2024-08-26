from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Event, Rsvp, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']


class EventSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location']


class RsvpSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Rsvp
        fields = ['id', 'user', 'event', 'response']


class CommentSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Comment
        fields = ['id', 'user', 'event', 'comment', 'created_at']
