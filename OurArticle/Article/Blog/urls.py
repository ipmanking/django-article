from django.urls import path
# from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('',views.view_index, name = "view_index"),
    path("listpic", views.view_about, name='view_listpic'),
    path("about", views.view_about , name = 'view_about'),
    path("newslistpic",views.view_newslistpic ,name="view_newslistpic"  ),
]