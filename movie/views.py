from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def home(request):
    #return HttpResponse('<h1>Welcome to Home page</h1>')
    #return render(request, 'home.html')
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(tittle__icontains=searchTerm)
    else:
        movies = Movie.objects.all()

     
    return render(request, 'home.html',{'searchTeam':searchTerm, 'movies':movies})


def about(request):
    return render(request,'about.html')

# Create your views here.
