from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.models import ModelMultipleChoiceField
from .models import *

from django import forms  


class MovieForm(forms.ModelForm):  
    class Meta:  
        model = Movie  
        fields = "__all__"          



class ActorForm(forms.ModelForm):  
    class Meta:  
        model = Actor  
        fields = "__all__"  