from django.shortcuts import render, get_object_or_404, redirect
from Covid.forms import RegisterForm
# Create your views here.
from .models import BlogPost
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.http import JsonResponse


def blog_post_list_view(request):
    qs = BlogPost.objects.all() # queryset-> list of python object
    template_name = 'blog_post_list.html'  # list out objects , could be search
    context = {'object_list': qs}
    return render(request, template_name, context)


def blog_post_create_view(request):  
    template_name = 'blog_post_create.html'
    context = {'form': None}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug=None):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_update.html'
    context = {"object": obj, 'form': None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug=None):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_delete.html'
    context = {"object": obj}
    return render(request, template_name, context)



def Register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('loginpage')
    template_name = 'register.html'
    context = {'form':form}
    
    return render(request, template_name, context)


def loginpage(request):
    if request.user.is_superuser:
        return HttpResponseRedirect(reverse('admin:index'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponseRedirect(reverse('admin:index'))
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    template_name = 'login.html'
    return render(request, template_name)


@login_required(login_url='loginpage')
def logoutpage(request):
    logout(request)
    return redirect('loginpage') 


def choose_register(request):
    return render(request, 'choose_register.html')
