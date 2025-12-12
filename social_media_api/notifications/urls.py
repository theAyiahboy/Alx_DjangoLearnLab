from django.urls import path
from .views import NotificationListView, MarkNotificationReadView

urlpatterns = [
    # List all notifications for the logged-in user
    path('', NotificationListView.as_view(), name='notifications'),

    # Mark a specific notification as read
    path('<int:notification_id>/read/', MarkNotificationReadView.as_view(), name='notification-read'),
]
