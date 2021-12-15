from django.http import request
from . import views
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('/home',views.addmovie(),name='addmovie'), 
    path('addm', views.addmovie),  
    path('adda', views.addactor),  
    path('showa',views.showa),    
    path('showm',views.showm),  
    path('addaajax',views.addaajax,name='addaajax'),
    path('addmajax',views.addmajax,name='addmajax'),
    path('showmajax',views.showmajax,name='showmajax'),
    

]