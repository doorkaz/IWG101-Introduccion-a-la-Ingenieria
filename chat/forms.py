from django import forms
from django.shortcuts import render, redirect
from .models import ChatRoom, User
from allauth.account.forms import SignupForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

image_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/avatar/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}avatar/'.format(settings.MEDIA_URL),
)


def image_directory_path(instance, filename):
    return format(filename)

class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ["name", "description","tags","image"]
        labels = {
            "name": "Nombre",
            "description": "Descripción",
            "tags": "Etiquetas",
            "image": "Imagen"
        },
        help_texts = {
            'tags': "Los tags se separan por espacios o por comas",
        }

class CustomSignupForm(SignupForm):
    avatar = forms.ImageField(label='Avatar')
    bio = forms.CharField(label='Sobre mi',max_length=255,widget=forms.Textarea(attrs={'name':'body', 'rows':'3', 'cols':'30'}))
    discord = forms.CharField(label='Discord',max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Anonimo#1234'}),required=False)

    def clean_discord(self):
        discord = self.cleaned_data['discord']
        if get_user_model().objects.filter(discord=discord).exists():
            raise ValidationError("Ya existe un usuario con esta cuenta de discord.")
        return discord