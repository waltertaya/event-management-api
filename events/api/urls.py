from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('signup/', views.signup),
    path('events/', views.events),
    path('rsvp/', views.rsvp),
    path('rsvp/<int:pk>/', views.rsvp_detail),
    path('comments/', views.post_comment),
    path('comments/<int:pk>/', views.get_comments),
    path('comment/<int:pk>/', views.user_comment),
]