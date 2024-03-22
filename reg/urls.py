import reg.views.auth.views
from django.urls import path,include
from django.http import HttpResponse
from reg.views.auth import views
from reg.views.home import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),

    path('login', reg.views.auth.views.loginpage,name="login"),
    path('logout',reg.views.auth.views.logoutuser,name='logout'),
    path('register',reg.views.auth.views.register_user,name='register_user'),


    path('',reg.views.home.views.home, name='home'),
    path('search',reg.views.home.views.search_page,name="search"),
    path('course_scrap',reg.views.home.views.course_scrap,name='course_scrap')
]


