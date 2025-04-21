import json

from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationsConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add(
            "notifications",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            "notifications",
            self.channel_name
        )

    async def notification_create(self, event):

        message = event["message"]
        await self.send(text_data=json.dump({
            "type": "Notifications",
            "message": message
        }))