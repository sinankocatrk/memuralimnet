from django.contrib import admin
from django.urls import path
from . import views


app_name= "kontenjan"



urlpatterns = [
    path('kontenjan/', views.kontenjan,name= "kontenjan"), 
    # path('ebe21/', views.ebe21,name= "ebe21"), 
    # path('hemsire21/', views.hemsire21,name= "hemsire21"), 
    # path('ebe20/', views.ebe20,name= "ebe20"),

    # path('s2021/<str:id>', views.s2021,name= "s2021"),
    # path('ebe222/', views.ebe222,name= "ebe222"),
    # path('hemsire222/', views.hemsire222,name= "hemsire222"),
    path('s2021/', views.s2021,name= "s2021"),
    # path('s2021/<str:id>', views.s2021filter,name= "s2021filter"),

    path('s2021/<str:id>', views.s2021filter,name= "s2021filter"),
    


]
