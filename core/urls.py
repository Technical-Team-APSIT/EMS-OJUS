
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('event/<str:pk>', views.registerEvent, name='reg'),
    
]