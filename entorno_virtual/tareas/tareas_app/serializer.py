from rest_framework import serializers
from .models import Usuario, Proyecto, Tarea


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        # fields = ('nombre', 'correo_electronico', 'contrasena')
        fields = '__all__'


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        # fields = ('nombre', 'descripcion', 'fecha_inicio', 'fecha_finalizacioon')
        fields = '__all__'


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        # fields = ('nombre', 'descripcion', 'fecha_vencimiento', 'estado', 'idusuario', 'idproyecto')
        fields = '__all__'