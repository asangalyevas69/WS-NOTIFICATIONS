from django.db import models

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class Task(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "notification_create",
                "message": f"Task {self.title} was created!"
            }
        )

        return  super().save(*args, **kwargs)