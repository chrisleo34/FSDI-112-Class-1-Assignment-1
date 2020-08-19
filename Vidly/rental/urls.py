from django.urls import path
from . import views


# valid routes for rental app
urlpatterns = [
    path('', views.home, name="root"),
    path('home', views.home, name="home"),
    path('about', views.about, name="about"),
    path(r'contact', views.contact, name="contact"),

]
