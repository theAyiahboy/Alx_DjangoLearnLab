from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # ManyToMany to itself for followers
    followers = models.ManyToManyField("self", symmetrical=False, related_name="following", blank=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.created_at.strftime("%Y-%m-%d %H:%M")}'

class Like(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')  # prevents duplicate likes

    def __str__(self):
        return f"{self.user.username} liked post {self.post.id}"


class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented on post {self.post.id}"

