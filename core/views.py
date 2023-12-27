from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Signed, Rule
from datetime import date






def index(request):
    user = request.user
    events = Event.objects.prefetch_related('eventhead_set').all()
    
    context = {
        'events' : events,
        'user' : user,
    }
    return render(request, 'core/index.html', context)

def eventDetails(request,slug):
    user = request.user
    events = get_object_or_404(Event, slug=slug)
    rules = Rule.objects.filter(event = events)
    
    
    context = {
        'events' : events,
        'user' : user,
        'rules' : rules,
    }
    return render(request, 'core/event-detail.html', context)


def schedule(request):
    user = request.user
    day1 = Event.objects.filter(date=date(2024, 1, 3))
    day2 = Event.objects.filter(date=date(2024, 1, 4))
    day3 = Event.objects.filter(date=date(2024, 1, 5))
    day4 = Event.objects.filter(date=date(2024, 1, 6))

    context = {
        'day1': day1,
        'day2': day2,
        'day3': day3,
        'day4': day4,
        'user': user,
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
        moodle_id = request.POST.get('moodle_id')
        password = request.POST.get('password')

        try:
            user = User.objects.get(moodle_id=moodle_id)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, moodle_id=moodle_id, password=password)

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
            fname = user.fname,
            lname = user.lname,
            dept = user.dept, 
            year = user.year,
            ename = event.name

        )

    return HttpResponse(f'Signed up sucessfully for'+ event.name)

# Create your views here.
