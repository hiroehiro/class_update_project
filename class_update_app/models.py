from django.db import models
from datetime import datetime

# Create your models here.
class ClassModel(models.Model):
    classname=models.TextField(null=True)
    content=models.TextField(null=True)
    url=models.TextField(null=True)
    name=models.CharField(max_length=100,null=True)
    passworld=models.CharField(max_length=100,null=True)
    date=models.DateTimeField(auto_now_add=True)