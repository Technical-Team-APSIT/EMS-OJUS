from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages





def index(request):
    return render(request, 'core/index.html')


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

# Create your views here.
