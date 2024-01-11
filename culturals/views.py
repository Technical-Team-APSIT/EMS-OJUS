from django.shortcuts import render
from django.http import HttpResponse


def landing(request):
    return HttpResponse('Landing Page')

# Create your views here.
