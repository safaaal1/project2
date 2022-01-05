
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login, logout

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'Register_businessOwner.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,  instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile_businessOwner')
    return render(request, 'profile_businessOwner.html')
"""'
def register_businessowner(request):
    if request.method == "POST":
        form = Register_BusinessOwner(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            blogs = BlogPost.objects.all()
            return render(request, "home.html", {'blogs': blogs})
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = Register_BusinessOwner()
    return render(request=request, template_name="Register_businessOwner.html", context={'form': form})
"""
def login_businessowner(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponseRedirect(reverse('profile'))
            return redirect('profile')
        else:
            messages.info(request, 'Username or password is incorrect')
    template_name = 'login_businessOwner.html'
    return render(request, template_name)
