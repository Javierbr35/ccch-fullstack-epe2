from django.urls import path

from . import api_views
from . import views


urlpatterns = [
    path("", views.inicio, name="inicio"),

    # API existente de EPE2
    path(
        "api/resumen/",
        views.api_resumen_ccch,
        name="api_resumen_ccch",
    ),
    path(
        "api/solicitudes/",
        views.api_crear_solicitud,
        name="api_crear_solicitud",
    ),

    # API REST de proyectos para EPE3
    path(
        "api/proyectos/",
        api_views.ProyectoListCreateAPIView.as_view(),
        name="proyectos-list-create",
    ),
    path(
        "api/proyectos/exportar.xml",
        api_views.ProyectoExportarXMLAPIView.as_view(),
        name="proyectos-exportar-xml",
    ),
    path(
        "api/proyectos/<int:pk>/",
        api_views.ProyectoDetailAPIView.as_view(),
        name="proyecto-detail",
    ),
]