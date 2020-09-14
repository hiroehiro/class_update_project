#from django.db import models
from django.db.models import CharField, Model,DateTimeField
from datetime import datetime
from django_mysql.models import ListTextField

# Create your models here.
class ClassModel(Model):
    classname=ListTextField(base_field=CharField(max_length=100),size=100,null=True)
    content=ListTextField(base_field=CharField(max_length=100),size=100,null=True)
    url=ListTextField(base_field=CharField(max_length=100),size=100,null=True)
    name=CharField(max_length=100,null=True)
    passworld=CharField(max_length=100,null=True)
    date=DateTimeField(auto_now_add=True)
