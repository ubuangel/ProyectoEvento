from django.urls import path,include
from ajax import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('email_validar_para_agregar_ec/', views.agregar_ec_email_validar, name='add_ec_email_validate'),
    path('agregar_ec_datos_a_database/', views.agregar_ec_datos_a_database, name='add_ec_data_to_database'),
    path('desactivar_equipo/', views.desactivar_equipo, name='disable_club'),
    path('activar_equipo/', views.activar_equipo, name='activar_equipo'),
    path('eliminar_ec/', views.eliminar_ec, name='eliminar_ec'),
    path('registrar_participante/',views.registrar_participante,name="register_perticipant"),
    path('comprobar_datos_participante/',views.comprobar_datos_participante,name="check_perticipate_data"),
    path('eviaremail/',views.eviaremail,name="sendemail"),
    path('actualizar_perfil/',views.actualizar_perfil,name="update_profile"),
    path('cambiar_contraseña/',views.cambiar_contraseña,name="change_password"),
    path('editar_evento/',views.editar_evento,name="edit_event"),
    path('aprobar_miembro_request/',views.aprobar_miembro_request,name="approve_member_request"),
    path('eliminar_miembro_request/',views.eliminar_miembro_request,name="remove_member_request"),

    # path('shownews/',views.shownews,name="shownews"),

]
