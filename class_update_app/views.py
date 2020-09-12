from django.views.generic import ListView,CreateView,DetailView
from .models import ClassModel
from django.urls import reverse_lazy
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


