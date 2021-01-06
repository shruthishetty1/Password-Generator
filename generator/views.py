from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html')#passing the parameter and path of the html file 

def password(request):
    paswrd = ""
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',12))
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%&'))
        
    for i in range(length):
        paswrd += random.choice(characters)
    return render(request,'generator/password.html',{'password':paswrd})#passing the parameter to the website


