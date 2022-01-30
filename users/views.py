from django.shortcuts import render , get_object_or_404 , reverse , redirect
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect , HttpResponse
from django.db import IntegrityError
from django.contrib.auth.models import User 
from django.views.generic import DetailView
from django.contrib import messages

from users.models import Profile
from users.forms import ProfileUpdateForm , UserUpdateForm


# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:    
            login(request, user)
            return redirect('seminar:home')

        else:
            return render(request, "users/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect('seminar:home')

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "users/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "users/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return redirect('seminar:home')
    else:
        return render(request, "users/register.html")

def profile_view(request , username):
        
    user = User.objects.get(username = username)
    querySet = Profile.objects.get(user = user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return render(request, 'seminar/home.html')
    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    u_form = UserUpdateForm(instance=user)
    p_form = ProfileUpdateForm(instance=querySet)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profile_details' : querySet        
    }

    return render(request , 'users/profile.html' , context)

def layout(request):
    return render(request , 'users/layout.html')


