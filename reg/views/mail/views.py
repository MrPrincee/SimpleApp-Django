from django.shortcuts import render, redirect

from reg.views.mail.forms import MailForm

from django.core.mail import send_mail


def mail_sender(request):
    form = MailForm(request.POST or None)
    if request.method == "POST":

        if form.is_valid():
            username = request.user.username if request.user.is_authenticated else None
            send_mail(subject=form.cleaned_data['subject'],message=form.cleaned_data['message'],from_email=username,recipient_list=[form.cleaned_data['receiver']])
            return redirect('home')

    return render(request,"mail/mail.html",{"form":form})