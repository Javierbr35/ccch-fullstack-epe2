from xml.etree.ElementTree import Element, SubElement, tostring

from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .models import ProyectoInvestigacion
from .serializers import ProyectoSerializer


class ProyectoListCreateAPIView(generics.ListCreateAPIView):
    """
    GET  /api/proyectos/
    POST /api/proyectos/
    """

    queryset = ProyectoInvestigacion.objects.select_related(
        "investigador_principal"
    ).all()
    serializer_class = ProyectoSerializer
    permission_classes = [AllowAny]


class ProyectoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/proyectos/<id>/
    PATCH  /api/proyectos/<id>/
    DELETE /api/proyectos/<id>/
    """

    queryset = ProyectoInvestigacion.objects.select_related(
        "investigador_principal"
    ).all()
    serializer_class = ProyectoSerializer
    permission_classes = [AllowAny]


class ProyectoExportarXMLAPIView(APIView):
    """
    GET /api/proyectos/exportar.xml
    """

    permission_classes = [AllowAny]

    def get(self, request):
        proyectos = ProyectoInvestigacion.objects.select_related(
            "investigador_principal"
        ).all()

        raiz = Element("proyectos")

        for proyecto in proyectos:
            nodo_proyecto = SubElement(
                raiz,
                "proyecto",
                {"id": str(proyecto.id)},
            )

            SubElement(nodo_proyecto, "codigo").text = proyecto.codigo
            SubElement(nodo_proyecto, "titulo").text = proyecto.titulo
            SubElement(nodo_proyecto, "area_cientifica").text = (
                proyecto.get_area_cientifica_display()
            )
            SubElement(nodo_proyecto, "estado").text = (
                proyecto.get_estado_display()
            )
            SubElement(nodo_proyecto, "investigador_principal").text = (
                proyecto.investigador_principal.nombre_completo
            )
            SubElement(nodo_proyecto, "fecha_inicio").text = (
                proyecto.fecha_inicio.isoformat()
            )

        contenido_xml = tostring(
            raiz,
            encoding="utf-8",
            xml_declaration=True,
        )

        respuesta = HttpResponse(
            contenido_xml,
            content_type="application/xml; charset=utf-8",
        )
        respuesta["Content-Disposition"] = (
            'attachment; filename="proyectos.xml"'
        )

        return respuesta