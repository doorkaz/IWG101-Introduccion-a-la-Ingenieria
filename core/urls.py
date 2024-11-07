from django.contrib import admin
from django.urls import path, include
from .views import Index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index.as_view()),
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #https://www.devhandbook.com/django/user-profile/

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)