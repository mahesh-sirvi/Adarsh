"""PostCard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from card import views

admin.site.site_header = "Adarsh Prints"
admin.site.site_title = "Adarsh Admin Portal"
admin.site.index_title = "Welcome to Ararsh Prints Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Song.as_view()),
    path('about', views.AboutUs.as_view()),
    path('contact', views.ContactUs.as_view()),
    path('products/sc01', views.Shreeji.as_view()),
    path('products/safari_silk', views.SafariSilk.as_view()),
    path('products/sonika', views.Sonika.as_view()),
    path('products/view_all', views.AllProducts.as_view()),
    path('search', views.Search.as_view()),
    path('cart', views.CartView.as_view()),
    path('products/sc02', views.SC02.as_view()),
    path('products/sc03', views.SC03.as_view()),
    path('products/sc04', views.SCO4.as_view()),
    path('products/sc05', views.SC05.as_view()),
    path('products/sc06', views.SC06.as_view()),
    path('products/sc07', views.SC07.as_view()),
    path('products/sc08', views.SC08.as_view()),
    path('products/sc09', views.SC09.as_view()),
    path('products/sc10', views.SC10.as_view()),
    path('products/sc11', views.SC11.as_view()),
    path('products/sc12', views.SC12.as_view()),
    path('register', views.Register.as_view()),
    path('login', views.Login_Adarsh.as_view()),
    path('buy', views.Buy.as_view()),


]
