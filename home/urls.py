from django.urls import  include, path
from home import views

urlpatterns = [
    
    path('', views.index, name = 'home'),
    path('home', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('booking', views.booking, name = 'booking'),
    path('Sign in', views.sign_in, name = 'sign in'),
    
]