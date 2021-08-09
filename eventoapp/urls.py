from django.contrib import admin
from django.urls import path,include
from eventoapp import views
from django.conf import settings
# from django.conf.urls.static import static
# manageevent.html
urlpatterns = [
    path('crear/', views.crearevento, name='crearevento'),
    path('hosted/', views.organizados_eventos, name='hostedevent'),
    path('eventounico/<str:eventname>', views.eventosunicos, name='eventosunicos'),
    path('participantes/', views.participantes, name='participantes'),
    path('participantes/<str:eventname>/', views.Detalles_par, name='Detalles_par'),
    #path('equipos/', views.equipos, name='allclubs')

]
# urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
