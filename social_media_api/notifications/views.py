from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

# ---------------------------
#   LIST NOTIFICATIONS
# ---------------------------
class NotificationListView(generics.ListAPIView):
    """
    Returns all notifications for the logged-in user.
    Sorted by newest first.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-read', '-timestamp')


# ---------------------------
#   MARK NOTIFICATION AS READ
# ---------------------------
class MarkNotificationReadView(APIView):
    """
    Allows a user to mark a notification as read.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, notification_id):
        try:
            notification = Notification.objects.get(id=notification_id, recipient=request.user)
        except Notification.DoesNotExist:
            return Response({"detail": "Notification not found."}, status=404)

        notification.read = True
        notification.save()
        return Response({"detail": "Notification marked as read."}, status=200)
