import json

from channels.generic.websocket import AsyncWebsocketConsumer
from registration.models import User
from mychat.models import Chat, Message
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.get_chat_room = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.get_chat_room
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        chat_id = text_data_json['room_id']
        author = text_data_json['author']
        await self.create_chat_message(author, chat_id, message)
        message_data = {
            'author': User.objects.get(pk=author).username,
            'message': message
        }
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message_data
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    @database_sync_to_async
    def create_chat_message(self, author, chat_id, message):
        user = User.objects.get(pk=author)
        chat = Chat.objects.get(pk=chat_id)
        Message.objects.create(chat=chat,author=user,message=message)

    @database_sync_to_async
    def get_chat_message(self, chat_id):
        message_list = Message.objects.filter(chat_id=chat_id)
        author=[el.author for el in message_list]
        print(author)
        message_author=[el for el in message_list]
        print(message_author)
        return message_list
