from django.db import models
from datetime import datetime


# Create your models here.


class Movie(models.Model):
    movie_name = models.CharField(max_length=50,default=None)
    rating = models.IntegerField(default=0)
    cast = models.IntegerField(default=1,blank=True)
    genre = models.CharField(max_length=20,default='raw',blank=True)
    release_data = models.DateTimeField(default=datetime.now(),blank=True)

    class Meta:
        ordering = ['movie_name']

    def __str__(self):
        return self. movie_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=30,default=None)
    age = models.IntegerField(default=0,blank=True)
    lead = models.BooleanField(default=True,blank=True)
    movie = models.ManyToManyField(Movie)

    class Meta:
        ordering = ['actor_name']

    def __str__(self):
        return self.actor_name
     

class muv(models.Model):
    movie_title = models.CharField(max_length=20,default=None,blank=True)
    muv = models.ForeignKey(Movie,on_delete=models.CASCADE)
    act = models.ManyToManyField(Actor)


    def __str__(self):
        return self.movie_title



class idbm(models.Model):
    movie_title = models.CharField(max_length=20,default=None,blank=True)
    muv = models.ManyToManyField(Movie)
    act = models.ManyToManyField(Actor)


    # def __str__(self):
    #     return self.movie_title



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return "Choice: {}, Question:{}".format(self.choice_text, self.question.question_text)

class MyManager(models.Manager):
    pass

class Emplo(models.Model):
    emp_id = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

    # def create(self,*args,**kwargs):
    #     self.emp_id = 'I-HONOIDA' + str(self.id)
    #     super(Emplo,self).create(*args,**kwargs)

    def save(self, *args, **kwargs): 
        super().save(*args, **kwargs)  
        if not 'I-HONOIDA' in self.emp_id:  
            self.emp_id = 'I-HONOIDA'+self.emp_id
            super().save(*args, **kwargs)


