from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from taggit.managers import TaggableManager
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser

chatroom_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/chatroom/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}chatroom/'.format(settings.MEDIA_URL),
)

avatar_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/avatar/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}avatar/'.format(settings.MEDIA_URL),
)


def image_directory_path(instance, filename):
    return format(filename)

class Chat(models.Model):
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey('ChatRoom', on_delete=models.CASCADE)

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255, null=True)
    state = models.BooleanField(default=True)
    image = models.ImageField(default='default.jpg',upload_to=image_directory_path, storage=chatroom_storage)
    tags = TaggableManager(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class CustomUser(AbstractUser):
    avatar = models.ImageField(default='default.jpg', upload_to=image_directory_path, storage=avatar_storage)
    bio = models.CharField(max_length=255, blank=False)
    discord = models.CharField(max_length=50, blank=False, null=True, unique=True)
    room = models.IntegerField(blank=False, null=True)