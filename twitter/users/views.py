from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from .forms import UserRegisterForm, ProfileUpdateForm
from django.contrib import messages

def registeruser(request):
    '''registers user'''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #messages.success(request, f'Account created for {username}.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def loginview(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        ps = request.POST.get('ps')
        user = authenticate(username = un, password = ps)
        print('-------', user)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request,'users/login.html')

def logoutview(request):
    logout(request)
    return redirect ('login')

def profile_update(request):
    pform = ProfileUpdateForm(instance= request.user.profile)
    if request.method == 'POST':
        pform = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if pform.is_valid():
            print('555555555555')
            pform.save()
            # try:
            #     profile =Profile.objects.create(user=request.user)    We can use this to create profile instance but instead use signals
            # except:
            #     pass
            return redirect('home')
    return render(request,'users/update_profile.html',{'pform':pform} )



