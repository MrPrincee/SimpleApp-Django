from django.urls import path, include
from .views import all_channel, create_channel, channel_chat

urlpatterns = [
    path('all_channel', all_channel, name='all_channel'),
    path('create_channel', create_channel, name='create_channel'),
    path("channel_chat/<int:channel_id>",channel_chat,name='channel_chat')
    ]
