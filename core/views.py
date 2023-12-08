from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Site setup')

# Create your views here.
