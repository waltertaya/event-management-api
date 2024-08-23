from django.urls import path
from . import views

urlpatterns = [
    path('event/', views.EventViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('rsvp/<int:pk>', views.RSVPViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('comment/', views.CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
]
