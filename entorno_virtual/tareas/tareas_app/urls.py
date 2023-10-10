from django.urls import include, path,path
from .views12 import UsuarioView

from rest_framework import routers
from tareas_app import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet, basename='usuarios')
router.register(r'proyectos', views.ProyectoViewSet, basename='proyectos')
router.register(r'tareas', views.TareaViewSet, basename='tareas')
urlpatterns = [
    path("", include(router.urls)),
]


#urlpatterns = [
#    path('listar_usuarios/',UsuarioView.as_view(),name='listar_usuarios'),
#    path('listar_usuarios/<int:id>',UsuarioView.as_view(),name='listar_usuarios'),
#]