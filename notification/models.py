from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Notification(models.Model):

    FOLLOWER = 'follower'
    LIKE = 'like'
    MENTION = 'mention'
    CHOICES = (
        (FOLLOWER, 'follower'),
        (LIKE, 'like'),
        (MENTION, 'mention')
    )
    to_user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)

    notification_type = models.CharField(max_length=20, choices=CHOICES)
    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='creatednotificatios', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']