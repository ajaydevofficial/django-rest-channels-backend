from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your models here.
class Notification(models.Model):
    message = models.CharField(null=False,default="", max_length=50)



@receiver(post_save, sender=Notification)
def SpaceHandler(sender, instance, created, **kwargs):
    if created:
        layer = get_channel_layer()
        async_to_sync(layer.group_send)('room_notifications', {
            'type': 'events_alarm',
            'content': instance.message
        })