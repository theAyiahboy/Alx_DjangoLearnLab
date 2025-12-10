# Social Media API

This is a mini social media backend built with **Django** and **Django REST Framework**.  
It supports user registration, authentication, profiles, posts, likes, comments, followers, and feed.

## Setup

1. Clone the repo:
git clone <your-repo-url>
cd Alx_DjangoLearnLab/social_media_api

2. Create a virtual environment and activate it:
python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # Mac/Linux

3. Install dependencies:
pip install django djangorestframework djangorestframework-authtoken

4. Apply migrations:
python manage.py makemigrations
python manage.py migrate

5. Run the server:
python manage.py runserver


## API Endpoints

- `/api/accounts/register/` → Register new user  
- `/api/accounts/login/` → Login and get token  
- `/api/accounts/profile/` → View & update profile  
- `/api/accounts/follow/<username>/` → Follow user  
- `/api/accounts/unfollow/<username>/` → Unfollow user  
- `/api/accounts/posts/` → List & create posts  
- `/api/accounts/posts/<post_id>/like/` → Like post  
- `/api/accounts/posts/<post_id>/unlike/` → Unlike post  
- `/api/accounts/posts/<post_id>/comment/` → Add comment  
- `/api/accounts/posts/<post_id>/comments/` → List comments  
- `/api/accounts/feed/` → Show posts from followed users

## Notes

- Use `Authorization: Token <your_token>` in headers for protected endpoints  
- Upload images via `multipart/form-data`  

python manage.py createsuperuser
http://127.0.0.1:8000/admin/
