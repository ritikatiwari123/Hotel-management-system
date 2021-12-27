from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from home.availability import logic

# Create your views here.

def index(request):
     return render(request, 'index.html')
     
    #return HttpResponse ("hello world this is my first project")
def home(request):
    # return HttpResponse ("hello world this is my home page") 
    return render(request, 'index.html')

def about(request):
     return render(request, 'about.html')    

def contact(request):
     if request.method =="POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          phone = request.POST.get('phone')
         
          desc = request.POST.get('desc')
          contact = Contact(name= name, email=email, phone=phone, desc=desc, date=datetime.today())
          contact.save()
          messages.success(request, 'Your message has been sent!')
     return render(request, 'contact.html') 

def booking(request):
     if request.method == "POST":
          room_category = request.POST.get('room_category')
          check_in = request.POST.get('check_in')
          check_in = request.POST.get('check_in')
          def form_valid(self, booking):
               
     
    # return HttpResponse ("hello world this is my booking page") 
     return render(request, 'booking.html') 


def sign_in(request):
    # return HttpResponse ("hello world this is my booking page") 
     return render(request, 'login.html') 


