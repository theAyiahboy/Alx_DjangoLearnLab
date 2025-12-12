from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    ProfileView,
    FollowUserView,
    UnfollowUserView,
)

urlpatterns = [
    # User registration and login
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    # User profile
    path('profile/', ProfileView.as_view(), name='profile'),

    # Follow/unfollow users
    path('follow/<int:pk>/', FollowUserView.as_view(), name='follow-user'),  # use pk
    path('unfollow/<int:pk>/', UnfollowUserView.as_view(), name='unfollow-user'),  # use pk
]
