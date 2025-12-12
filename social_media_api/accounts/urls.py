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
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
