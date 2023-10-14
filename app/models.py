from django.db import models
from django.urls import reverse


# Create your models here.
class School(models.Model):
    sname = models.CharField(max_length=20)
    sprincipal = models.CharField(max_length=20)
    slocation = models.CharField(max_length=20)


    def __str__(self):
        return self.sname


    def get_absolute_url(self):
        return reverse('detail',kwargs ={'pk':self.pk})
    
class Student(models.Model):
    stname = models.CharField(max_length = 20)
    stage = models.IntegerField()
    sname = models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return self.stname
    
