import json

from channels.generic.websocket import AsyncWebsocketConsumer
from registration.models import User
from mychat.models import Chat, Message
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.get_chat_room = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.get_chat_room

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        chat_id = text_data_json['room_id']
        author = text_data_json['author']
        await self.create_chat_message(author, chat_id, message)
        message_data = {
            'author': User.objects.get(pk=author).id,
            'avatar': User.objects.get(pk=author).avatar.url,
            'time': str(Message.objects.filter(chat_id=chat_id).last().pub_date)[:16],
            'message': message
        }

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message_data
            }
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))

    @database_sync_to_async
    def create_chat_message(self, author, chat_id, message):
        user = User.objects.get(pk=author)
        chat = Chat.objects.get(pk=chat_id)
        Message.objects.create(chat=chat, author=user, message=message)
