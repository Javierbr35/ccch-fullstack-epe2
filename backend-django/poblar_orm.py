import os
import sys
from datetime import date
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ccch_core.settings')
django.setup()

from nucleo_cientifico.models import (
    Investigador,
    ProyectoInvestigacion,
    PublicacionCientifica,
    SolicitudComunidad,
)


def poblar_datos():
    print("Iniciando carga de datos científicos en PostgreSQL (ccch_db)...")

    inv1, _ = Investigador.objects.get_or_create(
        correo="camila.valdes@uchile.cl",
        defaults={
            "nombre_completo": "Dra. Camila Valdés Muñoz",
            "orcid": "0000-0002-1825-0097",
            "grado_academico": "PhD",
            "institucion": "Universidad de Chile",
            "especialidad": "Astrofísica Observacional y Ciencia de Datos",
            "biografia": "Investigadora asociada en procesamiento de grandes volúmenes de datos astronómicos en el norte de Chile.",
            "activo": True,
        },
    )

    inv2, _ = Investigador.objects.get_or_create(
        correo="rodrigo.aravena@usach.cl",
        defaults={
            "nombre_completo": "Dr. Rodrigo Aravena Soto",
            "orcid": "0000-0003-4120-8812",
            "grado_academico": "PhD",
            "institucion": "Universidad de Santiago de Chile (USACH)",
            "especialidad": "Hidrógeno Verde y Almacenamiento Energético",
            "biografia": "Especialista en celdas de combustible y transición energética sostenible en zonas áridas.",
            "activo": True,
        },
    )

    inv3, _ = Investigador.objects.get_or_create(
        correo="fernanda.sepulveda@puc.cl",
        defaults={
            "nombre_completo": "Mg. Fernanda Sepúlveda Rojas",
            "orcid": "0000-0001-9432-5510",
            "grado_academico": "Magister",
            "institucion": "Pontificia Universidad Católica de Chile",
            "especialidad": "Bioinformática y Genómica Marina",
            "biografia": "Dedicada al análisis genómico de microorganismos extremófilos de la corriente de Humboldt.",
            "activo": True,
        },
    )

    proy1, _ = ProyectoInvestigacion.objects.get_or_create(
        codigo="CCCH-2026-001",
        defaults={
            "titulo": "Clasificación Automatizada de Supernovas mediante Redes Neuronales",
            "area_cientifica": "ASTRO",
            "resumen": "Implementación de modelos de aprendizaje profundo para detectar eventos transitorios en observatorios del desierto de Atacama.",
            "investigador_principal": inv1,
            "estado": "EJECUCION",
            "presupuesto_clp": 45000000,
            "fecha_inicio": date(2026, 3, 15),
        },
    )

    proy2, _ = ProyectoInvestigacion.objects.get_or_create(
        codigo="CCCH-2026-002",
        defaults={
            "titulo": "Optimización de Electrolizadores Solares para Producción de Hidrógeno Verde",
            "area_cientifica": "ENERGIA",
            "resumen": "Evaluación térmica y electroquímica de prototipos fotovoltaicos acoplados en la Región de Antofagasta.",
            "investigador_principal": inv2,
            "estado": "EJECUCION",
            "presupuesto_clp": 62000000,
            "fecha_inicio": date(2026, 4, 1),
        },
    )

    proy3, _ = ProyectoInvestigacion.objects.get_or_create(
        codigo="CCCH-2026-003",
        defaults={
            "titulo": "Bioprospección Enzimática en Ecosistemas Costeros del Sur de Chile",
            "area_cientifica": "BIO",
            "resumen": "Identificación de enzimas activas a bajas temperaturas con potencial aplicación biotecnológica e industrial.",
            "investigador_principal": inv3,
            "estado": "REVISION",
            "presupuesto_clp": 38500000,
            "fecha_inicio": date(2026, 5, 10),
        },
    )

    PublicacionCientifica.objects.get_or_create(
        doi="10.1051/0004-6361/202648910",
        defaults={
            "titulo": "Deep Learning Pipelines for Real-Time Transient Detection in Chilean Skies",
            "proyecto": proy1,
            "autor_principal": inv1,
            "revista_o_congreso": "Astronomy & Astrophysics Journal",
            "anio_publicacion": 2026,
            "resumen_abstract": "Presentamos una arquitectura convolucional capaz de clasificar alertas astronómicas en menos de 120 milisegundos.",
            "url_documento": "https://doi.org/10.1051/0004-6361/202648910",
        },
    )

    PublicacionCientifica.objects.get_or_create(
        doi="10.1016/j.ijhydene.2026.07.042",
        defaults={
            "titulo": "Solar-to-Hydrogen Efficiency Benchmarks under High Irradiance in Atacama",
            "proyecto": proy2,
            "autor_principal": inv2,
            "revista_o_congreso": "International Journal of Hydrogen Energy",
            "anio_publicacion": 2026,
            "resumen_abstract": "Resultados experimentales tras 12 meses de operación continua de celdas PEM alimentadas por energía solar concentrada.",
            "url_documento": "https://doi.org/10.1016/j.ijhydene.2026.07.042",
        },
    )

    SolicitudComunidad.objects.get_or_create(
        correo_contacto="matias.contreras@ipchile.cl",
        tipo_solicitud="INCORPORACION",
        defaults={
            "nombre_solicitante": "Matías Contreras Vega",
            "institucion_origen": "IPCHILE Sede República",
            "mensaje": "Solicito incorporación como estudiante investigador en el área de ciencia de datos aplicada.",
            "estado_revision": "PENDIENTE",
        },
    )

    print("Carga completada con éxito:")
    print(f" - Investigadores: {Investigador.objects.count()}")
    print(f" - Proyectos: {ProyectoInvestigacion.objects.count()}")
    print(f" - Publicaciones: {PublicacionCientifica.objects.count()}")
    print(f" - Solicitudes: {SolicitudComunidad.objects.count()}")


if __name__ == "__main__":
    poblar_datos()