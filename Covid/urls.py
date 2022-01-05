"""Covid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

from .views import decrease, home_page, increase
from django.contrib import admin
from django.urls import path, re_path, include
from blog.views import (
    blog_post_create_view,
    blog_post_detail_view,
    blog_post_list_view,
    blog_post_update_view,
    blog_post_delete_view,
    Register,
    loginpage,
    logoutpage,
    choose_register,
)
from.views import (
 home_page,
 about_page,
 contact_page,
 example_page,
 instructions,
 menu,
 HealthAndCare,
 Markets,
 Restaurants,
 To_Use,
 adminpage,
 adminprofile,
 DeleteUsers,
 delete_user,
 ShowRestaurants,
 places,
 UsersTable,
about_place,
rules_place,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page,name='home'),
    path('blog/', blog_post_list_view),
    path('blog/<str:slug>/', blog_post_detail_view),
    path('about/', about_page,name='about'),
    path('contact/', contact_page,name='contact'),
    path('instructions',instructions,name ='ins'),
    path('menu', menu,name='menu'),
    path('HealthAndCare', HealthAndCare,name='HealthAndCare'),
    path('Markets', Markets,name='Markets'),
    path('Restaurants', Restaurants,name='Restaurants'),
    path('register/', Register , name='Register'),
    path('login/', loginpage , name='loginpage'),
    path('logout/', logoutpage , name='logout'),
    path('increase/<int:blogId>/<int:pop>', increase , name='increase'),
    path('decrease/<int:blogId>/<int:pop>', decrease , name='decrease'),

    path('decrease',decrease, name='decrease'),
    path('To_Use', To_Use, name='To_Use'),
    path('adminpage/', adminpage, name='adminpage'),
    path('adminprofile/', adminprofile, name='adminprofile'),
    path('choose_register/', choose_register , name='choose_register'),
    path('DeleteUsers', DeleteUsers, name='DeleteUsers'),
    path('delete_user/<user_id>',delete_user,name="delete_user"),
    path('ShowRestaurants', ShowRestaurants, name='ShowRestaurants'),
    path('places', places , name='places'),
    path('UsersTable', UsersTable, name='UsersTable'),
    path('contact/', include('Contact.urls')),
    path('account/', include('account.urls')),
    path('about_place', about_place , name='about_place'),
    path('rules', rules_place , name='rules'),
]
