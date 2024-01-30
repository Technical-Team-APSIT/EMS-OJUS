from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import GSigned
from django.contrib import messages





def landing(request):
    return render(request, "landing.html")

def culturals(request):
    return render(request, 'culturals/index.html')

def schedule(request):
    return render(request, 'culturals/schedule.html')

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
# Create your views here.
