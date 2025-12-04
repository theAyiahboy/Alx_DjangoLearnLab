from django.contrib import admin
from .models import Profile  # add Post if you have it

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
