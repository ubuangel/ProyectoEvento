from django.contrib import admin
from django.urls import path,include
from equipo import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.equipoHome, name='equipoHome'),
    path('settings/', views.settings, name='settings'),
    path('requests/', views.requests, name='mem_requests'),
    path('miembros/', views.miembros, name='miembros'),
    path('actualizar_email/', views.actualizar_email, name='actualizar_email'),
    path('galeria/', views.galeria, name='actualizar_galeria'),
    path('actualizar_description/', views.actualizar_description, name='actualizar_description'),
    #path('equipos/', views.equipos, name='allclubs'),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
