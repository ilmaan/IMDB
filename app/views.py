from django.shortcuts import render
from django.shortcuts import render, redirect  
import io
from .forms import *
from app.models import *

# Create your views here.


def addmovie1(request):
    if request.method == 'POST':
        movie_name = request.POST['movie_name']
        rating = request.POST['rating']
        cast = request.POST['cast']
        genre = request.POST['genre']

        adm = Movie(movie_name=movie_name,rating=rating,cast=cast,genre=genre)
        adm.save()

    else:
        return render(request,'index.html')    


def addmovie(request):  
    if request.method == "POST":  
        form = MovieForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/showm')  
            except:  
                pass  
    else:  
        form = MovieForm()  
    return render(request,'index.html',{'form':form,'movie':True})  


def addactor(request):  
    if request.method == "POST":  
        form = ActorForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/showa')  
            except:  
                pass  
    else:  
        form = ActorForm()  
    return render(request,'index.html',{'form':form})  

    


def showm(request):  
    movies = Movie.objects.all()  
    return render(request,"show.html",{'movies':movies})  


def showa(request):  
    actors = Actor.objects.all()  
    return render(request,"show.html",{'actors':actors})  


    