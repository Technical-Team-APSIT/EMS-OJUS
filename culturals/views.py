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
        if entry.scanned == False:
            entry.scanned = True
            entry.save()
            messages.success(request, "Entry Valid")
        else:
            messages.warning(request, "This code has already been scanned.")
    return render(request, 'culturals/scanner.html')

@login_required(login_url='login')
def ghanekar(request):
   
    user = request.user
    signed = False
    existing_registration = GSigned.objects.filter(participant=user)
    if existing_registration:
            signed = True
            
    total = GSigned.objects.count()
    print(total)

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
                scanned = False,
            )
            if not created:
                messages.warning(request, f'Something is wrong with you.')
        else:
            messages.error(request, 'Registrations are closed. Please try again next semester.')


    context = {
        'user': user,
        'signed': signed,
    }

    
    return render(request, 'culturals/ghanekar.html', context)


def events(request):
    events = Event.objects.all()
    day1 = Event.objects.filter(date=date(2024, 2, 26))
    day2 = Event.objects.filter(date=date(2024, 2, 27))
    day3 = Event.objects.filter(date=date(2024, 2, 28))
    day4 = Event.objects.filter(date=date(2024, 2, 29))

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

    if request.method == 'POST':
        if event.fill:
            # Check if the user is already registered for any event of that type
                existing_registration = Signed.objects.filter(participant=user)
                if existing_registration:
                    return redirect('error')

                signed_obj, created = Signed.objects.get_or_create(
                    participant=user,
                    event=event,
                    pname=request.POST.get('pname'),
                    dept=user.dept,
                    year=user.year,
                    ename=event.name,
                    contact = request.POST.get('contact'),
                )
                redirect('cultural')
                if not created:
                    messages.warning(request, f'You are already registered for the event.')
        
    context = {
        'user': user,
        'event': event,
    }

    return render(request, 'culturals/regForm.html', context)
# Create your views here.
