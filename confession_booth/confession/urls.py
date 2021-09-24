
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage, name='mainpageview' ),
    path('write_a_confession/', views.WriteConfessions, name='writeaconfession' ),
    path('confession_viewing/', views.ViewConfessions, name='confessionviewing' ),
]
