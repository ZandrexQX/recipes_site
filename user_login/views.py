from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def signupuser(request):
    if request.method =='GET':
        return render(request, 'signupuser.html', {'form':UserCreationForm()})
    else:
        # Create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST.get('password'))
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signupuser.html', {'form':UserCreationForm(), 'error':'Name used'})
        else:
            #incorrect password
            return render(request, 'signupuser.html', {'form':UserCreationForm(), 'error':'Passwords not indent'})

def loginuser(request):
    if request.method =='GET':
        return render(request, 'loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')

@login_required        
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
