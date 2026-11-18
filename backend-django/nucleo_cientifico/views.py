import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import (
    Investigador,
    ProyectoInvestigacion,
    PublicacionCientifica,
    SolicitudComunidad,
)


def inicio(request):
    investigadores = Investigador.objects.filter(activo=True)
    proyectos = ProyectoInvestigacion.objects.select_related('investigador_principal').all()
    publicaciones = PublicacionCientifica.objects.select_related('autor_principal', 'proyecto').all()
    solicitudes = SolicitudComunidad.objects.all()[:5]

    contexto = {
        'investigadores': investigadores,
        'proyectos': proyectos,
        'publicaciones': publicaciones,
        'solicitudes': solicitudes,
        'total_investigadores': investigadores.count(),
        'total_proyectos': proyectos.count(),
        'total_publicaciones': publicaciones.count(),
    }
    return render(request, 'nucleo_cientifico/inicio.html', contexto)


def api_resumen_ccch(request):
    investigadores = list(
        Investigador.objects.filter(activo=True).values(
            'id',
            'nombre_completo',
            'orcid',
            'grado_academico',
            'institucion',
            'especialidad',
            'correo',
            'biografia',
        )
    )
    proyectos = [
        {
            'id': p.id,
            'codigo': p.codigo,
            'titulo': p.titulo,
            'area_cientifica': p.area_cientifica,
            'area_display': p.get_area_cientifica_display(),
            'resumen': p.resumen,
            'investigador_principal': p.investigador_principal.nombre_completo,
            'estado': p.estado,
            'estado_display': p.get_estado_display(),
            'presupuesto_clp': p.presupuesto_clp,
            'fecha_inicio': p.fecha_inicio.isoformat(),
        }
        for p in ProyectoInvestigacion.objects.select_related('investigador_principal').all()
    ]
    publicaciones = [
        {
            'id': pub.id,
            'titulo': pub.titulo,
            'autor_principal': pub.autor_principal.nombre_completo,
            'proyecto_codigo': pub.proyecto.codigo if pub.proyecto else None,
            'revista_o_congreso': pub.revista_o_congreso,
            'doi': pub.doi,
            'anio_publicacion': pub.anio_publicacion,
            'resumen_abstract': pub.resumen_abstract,
            'url_documento': pub.url_documento,
        }
        for pub in PublicacionCientifica.objects.select_related('autor_principal', 'proyecto').all()
    ]

    return JsonResponse({
        'investigadores': investigadores,
        'proyectos': proyectos,
        'publicaciones': publicaciones,
    })


@csrf_exempt
@require_http_methods(['POST'])
def api_crear_solicitud(request):
    try:
        datos = json.loads(request.body.decode('utf-8'))
        solicitud = SolicitudComunidad.objects.create(
            nombre_solicitante=datos.get('nombre_solicitante', '').strip(),
            correo_contacto=datos.get('correo_contacto', '').strip(),
            institucion_origen=datos.get('institucion_origen', '').strip(),
            tipo_solicitud=datos.get('tipo_solicitud', 'INCORPORACION'),
            mensaje=datos.get('mensaje', '').strip(),
        )
        return JsonResponse(
            {
                'ok': True,
                'id': solicitud.id,
                'mensaje': 'Solicitud registrada exitosamente en PostgreSQL.',
            },
            status=201,
        )
    except Exception as error:
        return JsonResponse({'ok': False, 'error': str(error)}, status=400)