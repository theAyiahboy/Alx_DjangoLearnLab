from django.urls import path
from .views import (
    RegisterView, LoginView, ProfileView,
    FollowUserView, UnfollowUserView,
    FollowUserByIdView, UnfollowUserByIdView
)
from .views import FollowUserView, UnfollowUserView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # username-based (kept for backwards compatibility)
    path('follow/<str:username>/', FollowUserView.as_view(), name='follow-by-username'),
    path('unfollow/<str:username>/', UnfollowUserView.as_view(), name='unfollow-by-username'),

    # id-based endpoints (task explicitly requires)
    path('follow/<int:user_id>/', FollowUserByIdView.as_view(), name='follow-by-id'),
    path('unfollow/<int:user_id>/', UnfollowUserByIdView.as_view(), name='unfollow-by-id'),

    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),

]
