
from django.urls import path
from . import views


urlpatterns = [
    path('', views.culturals, name='cultural'),
    path('signup', views.ghanekar, name='signup'),
    path('schedule', views.schedule, name='schedule'),
    path('heads', views.heads, name='heads'),
    path('council', views.council, name='council'),
    path('events', views.events, name='events'),
    path('register/<slug:slug>', views.regForm, name='reg'),
    path('team', views.team, name='team'),




    

]