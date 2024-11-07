from django.urls import path
from .views import Room, Profile, Index, CreateRoom, Search
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('createroom/', CreateRoom.as_view(), name='createroom'),
    path('search/', Search.as_view(), name='search_result'),
    path('<str:room_id>/', Room.as_view(), name='room'),
    path('profile/<str:profile_id>/', Profile.as_view(), name='profile'),    
]