from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Signed





def index(request):
    user = request.user
    events = Event.objects.all()
    context = {
        'events' : events,
        'user' : user,
    }
    return render(request, 'core/index.html', context)


def schedule(request):
    user = request.user
    events = Event.objects.all()
    context = {
        'events' : events,
        'user' : user,
    }
    return render(request, 'core/schedule.html', context)

def myEvents(request):
    user = request.user
    signed = Signed.objects.filter(participant=user)
    context = {
        'user' : user,
        'signed': signed,
    }
    return render(request, 'core/my-events.html', context)


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        id = request.POST.get('id')
        password = request.POST.get('password')

        try:
            user = User.objects.get(id=id)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, id=id, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Moodle id OR password does not exit')

    context = {'page': page}
    return render(request, 'core/login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def registerEvent(request, slug):
    event = Event.objects.get(slug=slug)
    user = request.user
    
    
    Signed.objects.get_or_create(
            participant = user,
            event = event,
        )

    return HttpResponse(f'Signed up sucessfully for'+ event.name)

# Create your views here.
