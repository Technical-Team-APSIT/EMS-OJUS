
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('schedule', views.schedule, name='schedule'),
    path('my-events', views.myEvents, name='my-events'),


    path('register/<slug:slug>', views.registerEvent, name='reg'),
    path('event/<slug:slug>', views.eventDetails, name='details'),


    
]