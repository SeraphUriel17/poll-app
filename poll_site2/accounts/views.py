import email
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from accounts.models import profile
from django.contrib import auth

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'accounts/signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],email=request.POST['email'],password=request.POST['password1'])
                user_profile = profile.objects.create(user=user)
                user_profile.phone_number = request.POST['phone_number']
                user_profile.save()
                auth.login(request,user)
                return render(request,'poll/home.html')
        else:
            return render (request,'accounts/signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return render(request,'poll/home.html')
        else:
            return render (request,'accounts/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return render(request,'poll/home.html')
