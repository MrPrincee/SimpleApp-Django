from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

from reg.utils import scrap, get_all_usernames


def loginpage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request ,username=username ,password=password)
            if user is not None:
                login(request ,user)
                if user.is_staff:
                    admin_url = reverse('admin:index')
                    return redirect(admin_url)
                else:
                    request.session['username'] = username
                    return redirect('home')

            else:
                print(user)
                messages.error(request, 'Wrong Password or Login')

        elif not username or not password:
            messages.error(request, 'Empty')

    context = {'page' :page}
    return render(request ,'reg.html' ,context)


def register_user(request):
    page = 'register'
    form = UserCreationForm

    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit='False')
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            pass
    return render(request,'reg.html',{'form':form})


def logoutuser(request):
    logout(request)
    return redirect('login')

