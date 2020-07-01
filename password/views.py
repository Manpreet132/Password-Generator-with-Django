from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):
    return render(request,'password/home.html')
# Create your views here.
def password(request):
    Characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        Characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        Characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        Characters.extend(list('0123456789'))
    length=int(request.GET.get('length',12))
    thepassword=''
    for x in range(length):
        thepassword=thepassword+random.choice(Characters)

    return render(request,'password/password.html',{'password':thepassword})
