from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Signed, Rule
from datetime import date
from django.contrib.auth import get_user_model
from django.db.models import Q
from datetime import datetime, date









def index(request, event_date= None):
    user = request.user
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    if event_date:
        events = Event.objects.prefetch_related('eventhead_set').filter(date= event_date)
    else:
        events = Event.objects.prefetch_related('eventhead_set').all()

    context = {
        'events' : events,
        'user' : user,
        'nums' : num_visits,
        
    }
    return render(request, 'core/index.html', context)


def credits(request):
    return render (request,'core/credits.html')






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
    day5 = Event.objects.filter(date=date(2024, 1, 7))


    context = {
        'day1': day1,
        'day2': day2,
        'day3': day3,
        'day4': day4,
        'day5': day5,
        'user': user,
    }
    return render(request, 'core/schedule.html', context)

def myEvents(request):
    user = request.user
    signed = Signed.objects.filter(Q(participant=user) | Q(participant2=user))
    context = {
        'user' : user,
        'signed': signed,
    }
    return render(request, 'core/my-events.html', context)


User = get_user_model()

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('landing')

    if request.method == 'POST':
        moodle_id = request.POST.get('moodle_id')
        password = request.POST.get('password')

        try:
            user = User.objects.get(moodle_id=moodle_id)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            return render(request, 'core/login.html', {'page': page})

        authenticated_user = authenticate(request, moodle_id=moodle_id, password=password)

        if authenticated_user is not None:
            login(request, authenticated_user)
            messages.success(request, f"You are now logged in as {user.fname}")
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Moodle id or password does not exist')

    context = {'page': page}
    return render(request, 'core/login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    redirect(request.META.get('HTTP_REFERER'))


def error(request):
    return render(request, '404.html')

from django.contrib import messages

@login_required(login_url='login')
def regForm(request, slug):
    event = get_object_or_404(Event, slug=slug)
    user = request.user

    if request.method == 'POST':
        if not event.is_doubles:
            # Check if the user is already registered for any event of that type
                existing_registration = Signed.objects.filter(participant=user, event__is_doubles=False).first()
                if existing_registration:
                    return redirect('error')

                signed_obj, created = Signed.objects.get_or_create(
                    participant=user,
                    event=event,
                    pname1=request.POST.get('pname1'),
                    dept=user.dept,
                    year=user.year,
                    ename=event.name,
                    contact = request.POST.get('contact'),
                )
                if not created:
                    messages.warning(request, f'You are already registered for the event.')
        else:
            a = request.POST.get('moodle_id2')
            u2 = User.objects.get(moodle_id=a)
            try:
                signed_obj, created = Signed.objects.get_or_create(
                    participant=user,
                    event=event,
                    participant2=u2,
                    pname1=request.POST.get('pname1'),
                    pname2=request.POST.get('pname2'),
                    dept=user.dept,
                    year=user.year,
                    ename=event.name,
                    contact = request.POST.get('contact'),
                    contact2 = request.POST.get('contact2'),
                )
                if not created:
                    messages.warning(request, f'You are already registered for the {event.name}.')
            except User.DoesNotExist:
                messages.warning(request, f'User with id {u2} does not exist')

        return redirect('my-events')

    context = {
        'user': user,
        'event': event,
    }

    return render(request, 'core/regForm.html', context)





# Create your views here.
