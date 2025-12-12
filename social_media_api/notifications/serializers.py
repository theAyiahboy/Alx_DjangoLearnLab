from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target_id = serializers.IntegerField(source='target.id', read_only=True)
    target_type = serializers.CharField(source='target.__class__.__name__', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'actor_username', 'verb', 'target_id', 'target_type', 'read', 'timestamp']
