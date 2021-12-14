from django.shortcuts import render
from django.shortcuts import render, redirect  
import io
from .forms import *
from app.models import *
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.



def addmovie(request):  
    # if request.method == "POST":  
    #     form = MovieForm(request.POST)  
    #     if form.is_valid():  
    #         try:  
    #             form.save()  
    #             return redirect('/showm')  
    #         except:  
    #             pass  
    # else:  
    formm = MovieForm()  

    forma = ActorForm()  

    actors = Actor.objects.all()  
    pa = Paginator(actors, 10)  
    page_number = request.GET.get('page')
    try:
        actor_obj = pa.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:    
        actor_obj = pa.page(1)
    except EmptyPage:
        actor_obj = pa.page(pa.num_pages)
        
    movies = Movie.objects.all() 
    pm = Paginator(movies,5)  
    page_number = request.GET.get('page')
    try:
        movie_obj = pm.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:    
        movie_obj = pm.page(1)
    except EmptyPage:
        movie_obj = pm.page(pm.num_pages)
    return render(request,'index.html',{'formm':formm,'forma':forma,'actors':actors,'movies':movies,'actor_obj':actor_obj,'movie_obj':movie_obj,})  


def addactor(request):  
    # if request.method == "POST":  
    #     form = ActorForm(request.POST)  
    #     if form.is_valid():  
    #         try:  
    #             form.save()  
    #             return redirect('/showa')  
    #         except:  
    #             pass  
    # else:  
    form = ActorForm()  
    actors = Actor.objects.all()  
    return render(request,'index.html',{'form':form,'actors':actors})  

    


def showm(request):  
    movies = Movie.objects.all()  
    return render(request,"show.html",{'movies':movies})  


def showa(request):  
    actors = Actor.objects.all()  
    return render(request,"show.html",{'actors':actors})  


def addaajax(request):
    if request.method == "POST":
        form = ActorForm(request.POST)
        
        instance = form.save()
        # ser_data = serializers.serialize('json',[instance,])

        # return JsonResponse({"instance":instance},status=200)
        return redirect('/showa')
        # else:
        #     return JsonResponse({"error": form.errors}, status=400)  

    return JsonResponse({"error": ""}, status=400)          



def addmajax(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        
        instance = form.save()
        # ser_data = serializers.serialize('json',[instance,])

        # return JsonResponse({"instance":instance},status=200)
        return redirect('/showm')
        # else:
        #     return JsonResponse({"error": form.errors}, status=400)  

    return JsonResponse({"error": ""}, status=400)     

    
def showmajax(request):
    if request.method == "GET":
        movies = Movie.objects.all() 
    return render(request,"show.html",{'movies':movies})      
        
