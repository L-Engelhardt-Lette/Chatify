from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message, Room

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    room, created = Room.objects.get_or_create(name=room_name)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    return render(request, 'chat/room.html', {'room_name': room_name, 'messages': messages})

@csrf_exempt
def add_message(request):
    if request.method == 'POST':
        username = request.POST.get('username', 'Anonymous')
        text = request.POST.get('text', '')
        room_name = request.POST.get('room', '')
        room, created = Room.objects.get_or_create(name=room_name)
        timestamp = timezone.now()
        message = Message.objects.create(user=username, room=room, text=text, timestamp=timestamp)
        response_data = {
            'user': message.user,
            'text': message.text,
            'timestamp': message.timestamp.strftime('%H:%M:%S'),
        }
        return JsonResponse(response_data)
