
import random
import os, sys
from typing import cast
import django

sys.path.extend(['/home/ilmaan/Desktop/Project/imdb/imdb'])
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imdb.settings')
django.setup()

from app.models import *


for i in range(5000):
    movie_name = ('Sample-movie'+str(i))
    rating = i
    casts = i*10
    genre = ('genre'+str(i))
    
    movie = Movie(movie_name=movie_name,rating=rating,cast=casts,genre=genre)
    movie.save()

    print(movie_name,rating,casts,genre) 

