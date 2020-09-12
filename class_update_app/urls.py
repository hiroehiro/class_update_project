from django.urls import path
from .views import ClassList,ClassCreate,ClassDetail

urlpatterns=[
    path("list/",ClassList.as_view(),name="list"),
    path("create/",ClassCreate.as_view(),name="create"),
    path("detali/<int:pk>",ClassDetail.as_view(),name="detail"),
]