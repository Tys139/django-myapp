from django.db import models
from django import forms
# Create your models here.



# creating a form
class GeeksForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()


class School(models.Model):
    name= models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Students(models.Model):
    sname=models.CharField(max_length=256)
    sage=models.PositiveIntegerField()
    school =models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)

    def __str__(self):
        return self.sname