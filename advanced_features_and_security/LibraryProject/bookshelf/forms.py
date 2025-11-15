from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from relationship_app.models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo')
