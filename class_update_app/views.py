from django.views.generic import ListView,CreateView,DetailView,DeleteView
from .models import ClassModel
from django.urls import reverse_lazy
import requests
from bs4 import BeautifulSoup
import re
from django.shortcuts import redirect
from django.shortcuts import render

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
    post.classname=[]
    post.url=[]
    post.content=[]
    for course in course_list[::-1]:
        course_name=str(course.find(class_=""))
        
        url=re.findall("https.*?>",course_name)[0][:-2]
        
        res = session.get(url)
        res.raise_for_status()
        soup=BeautifulSoup(res.text,"html.parser")
        course_content=soup.find(class_="course-content").text
        #course_content=str(course_content)
        #course_content=course_content.get_text()

        course_name=course_name.replace(",","")
        url=url.replace(",","")
        post.classname.append(course_name[82:113])
        post.classname.append(url)

        course_content=course_content.replace(",","")
        course_content=course_content.split()
        post.content+=course_content
        post.save()
    
    return redirect("detail",pk=pk)

    

class ClassDelete(DeleteView):
    template_name="delete.html"
    model=ClassModel
    success_url=reverse_lazy("list")


def comparefunc(request,pk):
    post=ClassModel.objects.get(pk=pk)
    prepost=ClassModel.objects.get(pk=pk-1)
    post.diffclassname=[]
    post.oldcontent=[]
    post.newcontent=[]

    post.oldcontent,post.newcontent=mayer_ses(post.content,prepost.content)
    
    sumcontent={}
    for i in range(max(len(post.oldcontent),len(post.newcontent))):
        if len(post.oldcontent)>=len(post.newcontent) and i>=len(post.newcontent):
            sumcontent[post.oldcontent[i]]="  "
        elif len(post.newcontent)>=len(post.oldcontent) and i>=len(post.oldcontent):
            sumcontent["  "]=post.newcontent
        else:
            sumcontent[post.oldcontent[i]]=post.newcontent[i]


    post.save()
    return render(request,"detail.html",{"object":post,"sumcontent":sumcontent})







def vk(v, index):
    if index in v:
        return v[index]
    return {
        'y': 0,
        'tree': []
        }

def meyer(a,b):
    m=len(a)
    n=len(b)
    v={}
    for d in range(m+n+1):
        for k in range(-d,d+1,2):
            if k<-n or k>m:
                continue                
            current_vk=vk(v,str(k))
            next_vk=None
            prev_vk=None
            if d!=0:
                can_move_prev_vk=False
                next_vk=vk(v,str(k+1))
                prev_vk=vk(v,str(k-1))
                if k==-d or k==-n:
                    can_move_prev_vk=False
                elif k==d or k==m:
                    can_move_prev_vk=True
                else:
                    if prev_vk["y"]>next_vk["y"]:
                        can_move_prev_vk=True
                    else:
                        can_move_prev_vk=False

                if can_move_prev_vk:
                    current_vk["y"]=prev_vk["y"]
                    current_vk['tree']=list(prev_vk['tree'])
                    current_vk['tree'].append(-1)
                else:
                    current_vk['y']=next_vk['y'] + 1
                    current_vk['tree']=list(next_vk['tree'])
                    current_vk['tree'].append(1)
            y = current_vk['y']
            x = k + y
            while x < m and y < n and a[x]==b[y]:
                current_vk['tree'].append(0)
                x = x + 1
                y = y + 1
            current_vk['y'] = y
            if x >= m and y >= n:
                return current_vk['tree']
            v[str(k)] = current_vk
            
def mayer_ses(a,b):
    a_ses=[]
    b_ses=[]
    actions=meyer(a,b)
    a_index=0
    b_index=0
    for action in actions:
        if action==0:
            a_ses.append(a[a_index])
            b_ses.append(b[b_index])
            a_index+=1
            b_index+=1
        elif action==1:
            b_ses.append("+"+b[b_index])
            b_index+=1
        else:
            a_ses.append("-"+a[a_index])
            a_index+=1
    return a_ses,b_ses,