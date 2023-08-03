from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse('<h1>Welcome to Home page</h1>')
    #return render(request, 'home.html')
    return render(request, 'home.html',{'name':'Martin Espitia'})

# Create your views here.
