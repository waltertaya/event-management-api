from django.urls import path
from . import views

urlpatterns = [
    path('rsvp/', views.RSVPAPIView.as_view()),
    path('comment/', views.CommentAPIView.as_view()),
]
