from channels.generic.websocket import AsyncWebsocketConsumer


class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add('tasks', self.channel_name)

    async def disconnect(self):
        await self.channel_layer.group_discard('tasks', self.channel_name)

    async def send_percentage(self, event):
        percentage = event['text']

        await self.send(percentage)