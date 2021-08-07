from django.urls import path
from usuario import views

urlpatterns = [
    path('', views.home, name='home'),
    path('evento/', views.evento_todos, name='evento_todos'),
    path('evento/<str:eventonombre>/', views.evento_unico, name='eventsingleuser'),
    path('avisos/<str:newsname>/', views.unicoaviso, name='unicoaviso'),
    path('noticia/<str:nombrenoticia>/', views.noticiain, name='noticiain'),
    path('perfil/',views.perfil,name="user_profile"),
    path('calendario/',views.calendario,name="calendar"),
    path('calendario/<str:label_name>',views.calendario_label,name="calendario_label"),
    path('equipos/',views.todos_equipos_usuarios ,name="todos_equipos_usuarios"),
    path('equipounico/<str:clubname>/',views.equipo_unico_usuario ,name="equipo_unico_usuario"),
    path('ec/<str:clubname>/',views.equipo_ec_usuario ,name="equipo_ec_usuario"),
    path('miembro/<str:clubname>/',views.miembro_req ,name="miembro_req"),
    path('galeria/<str:clubname>/',views.galeria ,name="galeria"),

]
