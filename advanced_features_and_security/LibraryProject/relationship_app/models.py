from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group  # <-- Add this import

# Author model
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Book model with custom permissions
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField(null=True, blank=True)

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
            ("can_view_book", "Can view book"),
        ]

    def __str__(self):
        return self.title

# Library model
class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

# Librarian model
class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# UserProfile for role-based access
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"



# Signal to automatically assign users to groups based on their role
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def assign_user_to_group(sender, instance, created, **kwargs):
    # Run only if profile exists
    try:
        profile = instance.userprofile
    except UserProfile.DoesNotExist:
        return

    if profile.role == 'Admin':
        group, _ = Group.objects.get_or_create(name='Admins')
    elif profile.role == 'Librarian':
        group, _ = Group.objects.get_or_create(name='Editors')
    else:
        group, _ = Group.objects.get_or_create(name='Viewers')

    instance.groups.add(group)
