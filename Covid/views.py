from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from blog.models import BlogPost
from account.models import Profile
from blog.views import blog_post_detail_view
from blog.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
def home_page(request):
    blogs = BlogPost.objects.all();
    return render(request, "home.html", {'blogs':blogs})


def about_page(request):
    return render(request, "about.html", {"title": "about"})


def contact_page(request):
    return render(request, "contact.html", {"title": "contact us"})


def instructions(request):
    return render(request, "instructions.html", {"title": "instructions"})

def menu(request):
    return render(request,"menu.html", {"title":"menu"})


def HealthAndCare(request):
    blogs = BlogPost.objects.all
    
    return render(request, "HealthAndCare.html", {'blogs': blogs})


def Markets(request):
    blogs = BlogPost.objects.all();

    return render(request, "Markets.html",{'blogs':blogs})


def Restaurants(request):
    blogs = BlogPost.objects.all();
    return render(request, "Restaurants.html", {'blogs':blogs})


def example_page(request):
    context       = {"title":"Example"}
    template_name = "hello_world.html"
    template_obj  = get_template(template_name)
    rendered_item = template_obj.render(template_name)
    return HttpResponse(rendered_item) #render(request,"hello_world.html",{"title": "contact us"})


def increase(request,blogId,pop):
    originalObj = BlogPost.objects.get(id = blogId)
    if originalObj.population == originalObj.capacity :
        blogs = BlogPost.objects.all();
        return render(request,"home.html",{'blogs':blogs})
    else:    
        originalObj.population = pop + 1
        originalObj.save()
        blogs = BlogPost.objects.all();
        return render(request,"home.html",{'blogs':blogs})

def decrease(request,blogId,pop):
    originalObj = BlogPost.objects.get(id = blogId)
    if originalObj.population == 0 :
        blogs = BlogPost.objects.all();
        return render(request,"home.html",{'blogs':blogs})
    originalObj.population = pop - 1
    originalObj.save()
    blogs = BlogPost.objects.all();
    return render(request,"home.html",{'blogs':blogs})


def To_Use(request):
    return render(request,"To_Use.html", {"title": "To_Use"})

def adminpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponseRedirect(reverse('adminprofile'))
            messages.info(request, 'You are not admin')
        else:
            messages.info(request, 'Username or password is incorrect')
    return render(request,"adminpage.html")



def adminprofile(request):
    return render(request,"adminprofile.html")


def DeleteUsers(request):
    users=user.objects.all()
    return render(request, "DeleteUsers.html", {'users': users})

def delete_user(request,user_id):
    users=user.objects.get(pk=user_id)
    users.delete()
    return redirect('DeleteUsers')

def ShowRestaurants(request):
    blogs = BlogPost.objects.all()
    return render(request,"ShowRestaurants.html",{'blogs': blogs})

def places(request):
    blogs = BlogPost.objects.all()
    return render(request,"places.html",{'blogs':blogs})

def UsersTable(request):
    users=user.objects.all()
    return render(request,"UsersTable.html",{'users':users})

def about_place(request):
    profile = Profile.objects.all()
    return render(request,"about_place.html",{'profile': profile})
def rules_place(request):
    profile = Profile.objects.all()
    return render(request,"rules.html",{'profile': profile})