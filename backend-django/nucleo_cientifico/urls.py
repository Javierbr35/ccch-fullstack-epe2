from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('api/resumen/', views.api_resumen_ccch, name='api_resumen_ccch'),
    path('api/solicitudes/', views.api_crear_solicitud, name='api_crear_solicitud'),
]