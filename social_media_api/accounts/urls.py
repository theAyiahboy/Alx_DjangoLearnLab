from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
]

from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('profile/', ProfileView.as_view(), name="profile"),
]

from .views import (
    RegisterView, LoginView, ProfileView,
    FollowUserView, UnfollowUserView
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('follow/<str:username>/', FollowUserView.as_view()),
    path('unfollow/<str:username>/', UnfollowUserView.as_view()),
]
from .views import PostListCreateView

urlpatterns += [
    path('posts/', PostListCreateView.as_view(), name='posts')
]

from .views import LikePostView, UnlikePostView, CommentPostView, ListCommentsView

urlpatterns += [
    path('posts/<int:post_id>/like/', LikePostView.as_view()),
    path('posts/<int:post_id>/unlike/', UnlikePostView.as_view()),
    path('posts/<int:post_id>/comment/', CommentPostView.as_view()),
    path('posts/<int:post_id>/comments/', ListCommentsView.as_view()),
]
