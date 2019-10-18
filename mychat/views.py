from django.shortcuts import render

from mychat.models import Chat, Message
from registration.models import User


def create_chat(request, recipient):
    recipient = User.objects.get(pk=recipient)
    all_chat = Chat.objects.all()
    for chat in all_chat:
        if request.user in chat.members.all():
            if recipient in chat.members.all():
                return list(request, chat.id)
    create = Chat.objects.create()
    create.members.add(request.user.id)
    create.members.add(recipient)
    create.save()
    return list(request, create.id)


def get_chat_room(request):
    room = {}
    user = request.user.id
    chat_room = Chat.objects.filter(members=user)
    for id in chat_room:
        message = Message.objects.filter(chat=id).last()
        room[id] = (id.members.first(), message)
    return render(
            request,
            'mychat/index.html',
            context={'user': user, 'room': room}
    )


def room(request, room_name):
    chat = Chat.objects.get(pk=room_name)
    if request.user in chat.members.all():
        return list(request, chat.id)


def list(request, chat_id):
    list_message = Message.objects.filter(chat_id=chat_id)
    return render(request, 'mychat/room.html', {
                                    'room_name_json': chat_id,
                                    'user': request.user.id,
                                    'list_message': list_message
            })
