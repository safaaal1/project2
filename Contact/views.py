from django.shortcuts import render
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
# Create your views here.
from blog.models import BlogPost
def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name == '':
            blogs = BlogPost.objects.all()
            return render(request, "home.html", {'blogs': blogs})
        else:
            contact.name = name
            contact.email = email
            contact.subject = subject
            contact.message = message
            contact.save()
    return render(request, 'contact.html')

