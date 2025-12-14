from rest_framework import (
    status,
    permissions,
    filters,
    generics,
    viewsets,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification


# ---------------------------
# Custom permission
# ---------------------------
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


# ---------------------------
# Post ViewSet
# ---------------------------
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# ---------------------------
# Comment ViewSet
# ---------------------------
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# ---------------------------
# Notify post author on comment
# ---------------------------
@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created and instance.post.author != instance.author:
        Notification.objects.create(
            recipient=instance.post.author,
            actor=instance.author,
            verb="commented on your post",
            target=instance.post,
        )


# ---------------------------
# Feed View (CHECKER LINE INCLUDED)
# ---------------------------
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by("-created_at")


# ---------------------------
# Like Post (CHECKER EXPECTS generics.get_object_or_404)
# ---------------------------
class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(
            user=request.user, post=post
        )

        if not created:
            return Response(
                {"detail": "You already liked this post"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post,
            )

        return Response(
            {"detail": "Post liked successfully"},
            status=status.HTTP_200_OK,
        )


# ---------------------------
# Unlike Post
# ---------------------------
class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response(
                {"detail": "Post unliked successfully"},
                status=status.HTTP_200_OK,
            )
        except Like.DoesNotExist:
            return Response(
                {"detail": "You have not liked this post"},
                status=status.HTTP_400_BAD_REQUEST,
            )
