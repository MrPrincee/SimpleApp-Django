from django.shortcuts import render, redirect
from reg.utils import scrap, get_all_usernames


def course_scrap(request):
    list1 = scrap()
    return render(request, 'scrap.html', {'list1': list1})


def home(request):
    username = request.user.username if request.user.is_authenticated else None
    return render(request, 'home.html', {'username': username})


def search_page(request):
    usernames = get_all_usernames()
    context = {'usernames': usernames}
    return render(request, 'search.html', context)