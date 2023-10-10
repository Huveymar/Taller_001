from django.shortcuts import render
from rest_framework import viewsets

from .models import Usuario, Proyecto, Tarea
from .serializer import UsuarioSerializer, ProyectoSerializer, TareaSerializer
# Create your views here.


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class ProyectoViewSet(viewsets.ModelViewSet):
    serializer_class = ProyectoSerializer
    queryset = Proyecto.objects.all()


class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    queryset = Tarea.objects.all()
