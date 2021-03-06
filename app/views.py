from django.shortcuts import render
from django.shortcuts import render, redirect  
import io
from .forms import *
from app.models import *
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import redis
import json
from django.conf import settings

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


# Create your views here.



@cache_page(60 * 10)
def addmovie(request,mpage=None,apage=None):  
    # if request.method == "POST":  
    #     form = MovieForm(request.POST)  
    #     if form.is_valid():  
    #         try:  
    #             form.save()  
    #             return redirect('/showm')  
    #         except:  
    #             pass  
    # else:  
    print("in the night")
    formm = MovieForm()  

    forma = ActorForm()  

    actors = Actor.objects.all()  
    pa = Paginator(actors, 10)  
    page_number = request.GET.get('page1')
    try:
        actor_obj = pa.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:    
        actor_obj = pa.page(1)
    except EmptyPage:
        actor_obj = pa.page(pa.num_pages)
        
    # movies = Movie.objects.all() 
    try:
        qs = cache.get('movies')
        print("DAta cache ", qs)
        if not qs:
            qs = Movie.objects.all()
            flag = cache.set('movies',qs)
            print("IN If", flag)
    except Exception as e:
        print('Exception:',e)

    cache.set('movies',qs)
    # pm = Paginator(qs,30)  
    # page_number = request.GET.get('page2')
    # try:
    #     movie_obj = pm.get_page(page_number)  # returns the desired page object
    # except PageNotAnInteger:    
    #     movie_obj = pm.page(1)
    # except EmptyPage:
    #     movie_obj = pm.page(pm.num_pages)
    return render(request,'index.html',{'formm':formm,'forma':forma,'actors':actors,'movies':qs,'actor_obj':actor_obj})  


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

    

cache_page(60*60)
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


@cache_page(60 * 10)
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
        
