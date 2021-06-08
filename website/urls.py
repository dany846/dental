from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name = "contact"),
    path('blog.html', views.contact, name = "blog"),
    path('about.html', views.contact, name = "about"),
    path('pricing.html', views.contact, name = "pricing"),
    path('service.html', views.contact, name = "service"),
]