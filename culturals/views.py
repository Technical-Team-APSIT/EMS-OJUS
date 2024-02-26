from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import GSigned, Event, Signed
from django.contrib import messages
from datetime import datetime, date






def landing(request):
    return render(request, "landing.html")

def culturals(request):
    return render(request, 'culturals/index.html')

def schedule(request):
    return render(request, 'culturals/schedule.html')

def heads(request):
    return render(request, 'culturals/heads.html')

def ghanekar(request):
    return render(request, 'culturals/ghanekar.html')

def council(request):
    return render(request, 'culturals/council.html')

def scan(request):

    if request.method == 'POST':
        mood = request.POST.get('decodeResult')
        entry = GSigned.objects.get(moodle_id=mood)
        if entry.scanned > 0:
            entry.scanned -= 1
            entry.save()
            messages.success(request, f"Entry Valid for {entry.pname}")
        else:
            messages.warning(request, "This code has already been scanned.")
    return render(request, 'culturals/scanner.html')

@login_required(login_url='login')
def ghanekar(request):
   
    user = request.user
    signed = False
    existing_registration = GSigned.objects.filter(participant=user)
    registrations_list = list(existing_registration.values())

    if existing_registration:
            signed = True
            
    total = GSigned.objects.count()

    if request.method == 'POST':
       
            # Check if the user is already registered for any event of that type
        if total <= 500:

            signed_obj, created = GSigned.objects.get_or_create(
                participant=user,
                moodle_id = user.moodle_id,
                pname=request.POST.get('pname'),
                dept=user.dept,
                year=user.year,
                contact = request.POST.get('contact'),
            )
            return redirect('signup')
            if not created:
                messages.warning(request, f'Something is wrong with you.')
        else:
            messages.error(request, 'Registrations are closed. Please try again next semester.')


    context = {
        'user': user,
        'signed': signed,
        'gsigned': registrations_list,
    }

    
    return render(request, 'culturals/ghanekar.html', context)


def events(request):
    events = Event.objects.all()
    day1 = Event.objects.filter(date=date(2024, 2, 26)).order_by('time')
    day2 = Event.objects.filter(date=date(2024, 2, 27)).order_by('time')
    day3 = Event.objects.filter(date=date(2024, 2, 28)).order_by('time')
    day4 = Event.objects.filter(date=date(2024, 2, 29)).order_by('time')

    context = {
        'events': events,
        'day1': day1,
        'day2':day2,
        'day3':day3,
        'day4':day4,
    }
    return render(request, "culturals/events.html", context)

@login_required(login_url='login')
def regForm(request, slug):
    event = get_object_or_404(Event, slug=slug)
    user = request.user
    already_filled = Signed.objects.filter(participant=user, event=event).exists()

    

    if request.method == 'POST':
        if event.fill:
            # Check if the user is already registered for any event of that type
                existing_registration = Signed.objects.filter(participant=user)
                if existing_registration:
                    return redirect(request.META.get('HTTP_REFERER'))

                signed_obj, created = Signed.objects.get_or_create(
                    participant=user,
                    event=event,
                    pname=request.POST.get('pname'),
                    dept=user.dept,
                    year=user.year,
                    ename=event.name,
                    contact = request.POST.get('contact'),
                )
                return redirect(request.META.get('HTTP_REFERER'))
                if not created:
                    messages.warning(request, f'You are already registered for the event.')
        
    context = {
        'user': user,
        'event': event,
        'filled': already_filled,
    }

    return render(request, 'culturals/regForm.html', context)

def team(request):
    return render(request, 'culturals/team.html')
# Create your views here.
