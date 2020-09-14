from django.views.generic import ListView,CreateView,DetailView,DeleteView
from .models import ClassModel
from django.urls import reverse_lazy
import requests
from bs4 import BeautifulSoup
import re
from django.shortcuts import redirect
# Create your views here.

class ClassList(ListView):
    template_name="list.html"
    model=ClassModel

class ClassDetail(DetailView):
    template_name="detail.html"
    model=ClassModel
    
class ClassCreate(CreateView):
    template_name="create.html"
    model=ClassModel
    fields=('name',"passworld")
    success_url=reverse_lazy("list")

def resultfunc(request,pk):
    post=ClassModel.objects.get(pk=pk)
    USER = post.name
    PASS = post.passworld
    session = requests.session()
    login_info = {
        "username":USER,
        "password":PASS,
        "back":"index.php",
        "mml_id":"0"
    }
    url_login = "https://lms.ealps.shinshu-u.ac.jp/2020/t/login/index.php"
    res = session.post(url_login, data=login_info)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"html.parser")
    course_list=soup.find_all(class_="coursename")
    post.classname=""
    post.url=""
    post.content=""
    for course in course_list[::-1]:
        course_name=str(course.find(class_=""))
        post.classname=post.classname+" , "+course_name[82:113]
        post.save()

        url=re.findall("https.*?>",course_name)[0][:-2]
        post.url=post.url+" , "+url
        post.save()

        res = session.get(url)
        res.raise_for_status()
        soup=BeautifulSoup(res.text,"html.parser")
        course_content=soup.find(class_="course-content")
        course_content=course_content.get_text()
        post.content=post.content+" , "+course_content
        post.save()
    

    return redirect("detail",pk=pk)

    

class ClassDelete(DeleteView):
    template_name="delete.html"
    model=ClassModel
    success_url=reverse_lazy("list")


