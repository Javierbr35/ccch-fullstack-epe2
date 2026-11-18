from django.db import models


class Investigador(models.Model):
    GRADOS = [
        ('PhD', 'Doctor(a) (PhD)'),
        ('Magister', 'Magíster'),
        ('Licenciado', 'Ingeniero(a) / Licenciado(a)'),
        ('Estudiante', 'Estudiante Investigador(a)'),
    ]

    nombre_completo = models.CharField(max_length=150, verbose_name='Nombre completo')
    orcid = models.CharField(max_length=50, unique=True, blank=True, null=True, verbose_name='Código ORCID')
    grado_academico = models.CharField(max_length=20, choices=GRADOS, default='PhD', verbose_name='Grado académico')
    institucion = models.CharField(max_length=150, verbose_name='Institución afiliada')
    especialidad = models.CharField(max_length=120, verbose_name='Área de especialidad')
    correo = models.EmailField(unique=True, verbose_name='Correo institucional')
    biografia = models.TextField(blank=True, verbose_name='Biografía breve')
    activo = models.BooleanField(default=True, verbose_name='Investigador activo')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Investigador'
        verbose_name_plural = 'Investigadores'
        ordering = ['nombre_completo']

    def __str__(self):
        return f"{self.nombre_completo} ({self.institucion})"


class ProyectoInvestigacion(models.Model):
    AREAS = [
        ('IA', 'Inteligencia Artificial y Ciencia de Datos'),
        ('BIO', 'Biotecnología y Salud'),
        ('ENERGIA', 'Energías Renovables y Medio Ambiente'),
        ('ASTRO', 'Astronomía y Física'),
        ('SOCIAL', 'Ciencias Sociales y Educación'),
    ]

    ESTADOS = [
        ('EJECUCION', 'En Ejecución'),
        ('REVISION', 'En Revisión'),
        ('FINALIZADO', 'Finalizado'),
        ('POSTULACION', 'En Postulación'),
    ]

    codigo = models.CharField(max_length=30, unique=True, verbose_name='Código de proyecto')
    titulo = models.CharField(max_length=250, verbose_name='Título del proyecto')
    area_cientifica = models.CharField(max_length=20, choices=AREAS, default='IA', verbose_name='Área científica')
    resumen = models.TextField(verbose_name='Resumen ejecutivo')
    investigador_principal = models.ForeignKey(
        Investigador,
        on_delete=models.CASCADE,
        related_name='proyectos',
        verbose_name='Investigador principal'
    )
    estado = models.CharField(max_length=20, choices=ESTADOS, default='EJECUCION', verbose_name='Estado')
    presupuesto_clp = models.PositiveIntegerField(default=0, verbose_name='Presupuesto (CLP)')
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio')
    fecha_termino = models.DateField(null=True, blank=True, verbose_name='Fecha de término')

    class Meta:
        verbose_name = 'Proyecto de Investigación'
        verbose_name_plural = 'Proyectos de Investigación'
        ordering = ['-fecha_inicio']

    def __str__(self):
        return f"[{self.codigo}] {self.titulo}"


class PublicacionCientifica(models.Model):
    titulo = models.CharField(max_length=300, verbose_name='Título de la publicación')
    proyecto = models.ForeignKey(
        ProyectoInvestigacion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='publicaciones',
        verbose_name='Proyecto asociado'
    )
    autor_principal = models.ForeignKey(
        Investigador,
        on_delete=models.CASCADE,
        related_name='publicaciones',
        verbose_name='Autor principal'
    )
    revista_o_congreso = models.CharField(max_length=200, verbose_name='Revista o Congreso')
    doi = models.CharField(max_length=100, unique=True, verbose_name='DOI')
    anio_publicacion = models.PositiveIntegerField(verbose_name='Año de publicación')
    resumen_abstract = models.TextField(verbose_name='Abstract')
    url_documento = models.URLField(blank=True, verbose_name='Enlace al artículo')
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Publicación Científica'
        verbose_name_plural = 'Publicaciones Científicas'
        ordering = ['-anio_publicacion', 'titulo']

    def __str__(self):
        return f"{self.titulo} ({self.anio_publicacion})"


class SolicitudComunidad(models.Model):
    TIPOS = [
        ('INCORPORACION', 'Incorporación como Investigador'),
        ('PROYECTO', 'Propuesta de Proyecto Colaborativo'),
        ('PUBLICACION', 'Publicación de Artículo'),
        ('CONSULTA', 'Consulta General'),
    ]

    ESTADOS_REV = [
        ('PENDIENTE', 'Pendiente'),
        ('EVALUACION', 'En Evaluación'),
        ('APROBADA', 'Aprobada'),
        ('RECHAZADA', 'Rechazada'),
    ]

    nombre_solicitante = models.CharField(max_length=150, verbose_name='Nombre del solicitante')
    correo_contacto = models.EmailField(verbose_name='Correo de contacto')
    institucion_origen = models.CharField(max_length=150, blank=True, verbose_name='Institución')
    tipo_solicitud = models.CharField(max_length=20, choices=TIPOS, default='INCORPORACION', verbose_name='Tipo de solicitud')
    mensaje = models.TextField(verbose_name='Mensaje o propuesta')
    estado_revision = models.CharField(max_length=20, choices=ESTADOS_REV, default='PENDIENTE', verbose_name='Estado de revisión')
    fecha_envio = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Solicitud de la Comunidad'
        verbose_name_plural = 'Solicitudes de la Comunidad'
        ordering = ['-fecha_envio']

    def __str__(self):
        return f"{self.nombre_solicitante} - {self.get_tipo_solicitud_display()}"