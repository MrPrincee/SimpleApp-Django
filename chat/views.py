from django.shortcuts import render, redirect
from chat.models import Channel, Message
from chat.forms import MessageForm, CreateChannelForm


def all_channel(request):
    channels = Channel.objects.all()
    return render(request, "all_channel.html",{'channels': channels})


def create_channel(request):
    form = CreateChannelForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            new_channel = Channel(name=name)
            new_channel.save()
            return redirect('all_channel')

    return render(request, 'create_channel.html', {'form': form})


def channel_chat(request,channel_id):
    form = MessageForm(request.POST or None)
    current_channel = Channel.objects.get(id=channel_id)
    channel_messages = Message.objects.filter(channel=current_channel)
    if request.method =='POST':
        if form.is_valid():
            message = form.cleaned_data['message']
            new_message = Message(message=message,channel=current_channel)
            new_message.save()
            return redirect('channel_chat',channel_id=current_channel.id)
    return render(request,"channel_chat.html",{'messages':channel_messages,"form":form,'current_channel':current_channel})