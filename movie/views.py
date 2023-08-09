from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def home(request):
    #return HttpResponse('<h1>Welcome to Home page</h1>')
    #return render(request, 'home.html')
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html',{'searchTerm':searchTerm} )


def about(request):
    return HttpResponse('<h1>Welcomw to About Page</h1>')

# Create your views here.
