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

@login_required(login_url='login')
def ghanekar(request):
   
    user = request.user
    signed = False
    existing_registration = GSigned.objects.filter(participant=user)
    if existing_registration:
            signed = True
            print(signed)

    if request.method == 'POST':
       
            # Check if the user is already registered for any event of that type


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


    context = {
        'user': user,
        'signed': signed,
    }

    
    return render(request, 'culturals/ghanekar.html', context)
# Create your views here.
