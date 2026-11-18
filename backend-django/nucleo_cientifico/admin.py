from django.contrib import admin
from .models import (
    Investigador,
    ProyectoInvestigacion,
    PublicacionCientifica,
    SolicitudComunidad,
)


@admin.register(Investigador)
class InvestigadorAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'grado_academico', 'institucion', 'especialidad', 'activo')
    list_filter = ('grado_academico', 'activo', 'institucion')
    search_fields = ('nombre_completo', 'orcid', 'correo', 'especialidad')


@admin.register(ProyectoInvestigacion)
class ProyectoInvestigacionAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'titulo', 'area_cientifica', 'investigador_principal', 'estado', 'fecha_inicio')
    list_filter = ('area_cientifica', 'estado')
    search_fields = ('codigo', 'titulo', 'resumen')


@admin.register(PublicacionCientifica)
class PublicacionCientificaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor_principal', 'revista_o_congreso', 'anio_publicacion', 'doi')
    list_filter = ('anio_publicacion',)
    search_fields = ('titulo', 'doi', 'revista_o_congreso')


@admin.register(SolicitudComunidad)
class SolicitudComunidadAdmin(admin.ModelAdmin):
    list_display = ('nombre_solicitante', 'tipo_solicitud', 'institucion_origen', 'estado_revision', 'fecha_envio')
    list_filter = ('tipo_solicitud', 'estado_revision')
    search_fields = ('nombre_solicitante', 'correo_contacto', 'mensaje')