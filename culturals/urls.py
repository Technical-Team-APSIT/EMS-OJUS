
from django.urls import path
from . import views


urlpatterns = [
    path('', views.culturals, name='cultural'),
    path('signup', views.ghanekar, name='signup'),
    path('schedule', views.schedule, name='schedule'),
    path('heads', views.heads, name='heads'),
    path('council', views.council, name='council'),



    

]