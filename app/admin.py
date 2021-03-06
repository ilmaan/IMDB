from django.contrib import admin

from app.models import Movie
from .models import *

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie_name','rating','cast','genre','release_data']



@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['actor_name']


@admin.register(muv)
class muvAdmin(admin.ModelAdmin):
    list_display = ['movie_title']

@admin.register(idbm)
class idbmAdmin(admin.ModelAdmin):
    list_display = ['movie_title']


admin.site.register(Question)


admin.site.register(Choice)


admin.site.register(Emplo)
