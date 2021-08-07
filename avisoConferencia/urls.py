from django.contrib import admin
from django.urls import path,include
from avisoConferencia import views
urlpatterns = [
    path('agregaravisos/', views.agregaravisos, name='agregaravisos'),
    path('agregarnoticias/', views.agregarnoticias, name='agregarnoticias'),
    path('todoavisos/',views.todoavisos,name="todoavisos"),
    path('eliminaraviso/<int:id>',views.eliminaraviso,name="eliminaraviso"),
    path('noticias/',views.todonoticias,name="todonoticias"),
    path('eliminarnoticia/<int:id>',views.eliminarnoticia,name="eliminarnoticia"),

]
