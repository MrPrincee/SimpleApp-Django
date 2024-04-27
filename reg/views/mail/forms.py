from django import forms


class MailForm(forms.Form):
    subject = forms.CharField(label="Subject",max_length=100)
    message = forms.CharField(label='Message')
    receiver = forms.CharField(label='Receiver')
