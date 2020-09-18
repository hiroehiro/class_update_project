#from django.db import models
from django.db.models import CharField, Model,DateTimeField,IntegerField
from datetime import datetime
from django_mysql.models import ListTextField

# Create your models here.
class ClassModel(Model):
    classname=ListTextField(base_field=CharField(max_length=100),size=100,null=True)
    diffclassname=ListTextField(base_field=CharField(max_length=100),size=100,null=True)
    content=ListTextField(base_field=CharField(max_length=100),size=100,null=True)
    oldcontent=ListTextField(base_field=CharField(max_length=100),size=100,null=True)
    newcontent=ListTextField(base_field=CharField(max_length=100),size=100,null=True)
    lenclass=IntegerField(null=True)
    url=ListTextField(base_field=CharField(max_length=100),size=100,null=True)
    name=CharField(max_length=100,null=True)
    passworld=CharField(max_length=100,null=True)
    date=DateTimeField(auto_now_add=True)
