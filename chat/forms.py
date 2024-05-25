from django import forms


class MessageForm(forms.Form):
    message = forms.CharField(label='Message',max_length=1000,error_messages=None)


class CreateChannelForm(forms.Form):
    name = forms.CharField(label='Name')