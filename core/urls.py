
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:event_date>', views.index, name='filtered'),
    path('team', views.credits, name='team'),


    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('schedule', views.schedule, name='schedule'),
    path('my-events', views.myEvents, name='my-events'),


    path('register/<slug:slug>', views.regForm, name='reg'),
    path('event/<slug:slug>', views.eventDetails, name='details'),


    
]