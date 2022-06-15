from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

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
        if user is not None:
            login(request, user)
            return redirect('update-profile')
    return render(request,'users/login.html')

def logoutview(request):
    logout(request)
    return redirect ('login')

# def profile(request):
#     if request.method == 'POST':
#         uform = UserUpdateForm(request.POST, instance=request.user)
#         pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)

#         if uform.is_valid() and pform.is_valid():
#             uform.save()
#             pform.save()
#             print('------------')
#             #messages.success(request, f'Account has been updated.')
#             return redirect('home')
#     else:
#         uform = UserUpdateForm(instance=request.user)
#         pform = ProfileUpdateForm(instance=request.user)

#     return render(request, 'users/profile.html', {'uform': uform, 'pform': pform})

def profile(request):
    pform = ProfileUpdateForm()
    if request.method == 'POST':
        pform = ProfileUpdateForm(request.POST, request.FILES)
        if pform.is_valid():
            pform.instance.user = request.user
            pform.save()
            return redirect('home')
    return render(request,'users/profile.html',{'pform':pform})
