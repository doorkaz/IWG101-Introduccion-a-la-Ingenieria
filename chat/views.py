from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chat, ChatRoom
from .forms import ChatRoomForm
from django.db.models import Q
from django.conf import settings
from django.contrib.auth import get_user_model

class Index(View):
    def get(self, request):
        chatRooms = ChatRoom.objects.filter(state=True).order_by('-timestamp')
        return render(request, 'chats.html', {'rooms': chatRooms})


class Room(LoginRequiredMixin, View):
    def get(self, request, room_id):
        room = ChatRoom.objects.filter(id=room_id, state=True).first()
        connected_users = get_user_model().objects.filter(room=room.id)
        chats = []

        if room:
            chats = Chat.objects.filter(room=room)
        else:
            return redirect('index')
        return render(request, 'chatroom.html', {'room_id': room_id, 'chats': chats, 'room': room,'connected_users':connected_users})

class Profile(View):
    def get(self, request, profile_id):
        # https://stackoverflow.com/questions/24629705/django-using-get-user-model-vs-settings-auth-user-model
        profile = get_user_model().objects.filter(id=profile_id).first()
        room = ChatRoom.objects.filter(id=profile.room, state=True).first()

        return render(request, 'profile.html', {'profile': profile,'room': room})

class CreateRoom(LoginRequiredMixin, View):
    def get(self, request):
        form = ChatRoomForm(request.POST or None)
        return render(request, 'create.html', {"form": form})

    def post(self, request):
        form = ChatRoomForm(request.POST or None, request.FILES)

        if form is not None:
            if form.is_valid():
                chatroom = form.save(commit=False)
                chatroom.user = request.user
                chatroom.save()
                return redirect('index')
            else:
                return redirect('index')
        else:
            return redirect('index')

        
    
class Search(View):
    def get(self, request):
        query_type = request.GET['type']
        terms = request.GET['q']

        results = None

        if query_type == 'tags':
            query = Q()

            for word in terms.split():
                query = query | Q(tags__name__icontains=word)
            
            results = ChatRoom.objects.filter(query)
        elif query_type == 'name':
            results =  ChatRoom.objects.filter(name__icontains=terms)

        print(terms)

        return render(request, "search.html", {'results': results})