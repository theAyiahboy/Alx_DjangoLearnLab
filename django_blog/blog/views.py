# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib import messages

def register_view(request):
    """
    Handles user registration.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.save()
            # Profile created by signal; update fields from profile_form
            profile = user.profile
            profile.bio = profile_form.cleaned_data.get('bio')
            # handle avatar if provided
            if profile_form.cleaned_data.get('avatar'):
                profile.avatar = profile_form.cleaned_data.get('avatar')
            profile.save()
            login(request, user)  # auto-login after registration
            messages.success(request, "Registration successful. Welcome!")
            return redirect('home')  # change to your landing page
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'blog/register.html', {'form': form, 'profile_form': profile_form})

@login_required
def profile_view(request):
    """
    View and edit user profile.
    """
    user = request.user
    profile = user.profile
    if request.method == 'POST':
        # update user email if provided
        email = request.POST.get('email')
        if email:
            user.email = email
            user.save()
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'blog/profile.html', {'form': form, 'user': user})
