import { Component, OnInit, computed, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CcchApiService, Investigador, ProyectoInvestigacion, PublicacionCientifica } from './services/ccch-api.service';

@Component({ selector: 'app-root', imports: [FormsModule], templateUrl: './app.html', styleUrl: './app.css' })
export class App implements OnInit {
  private readonly apiService = inject(CcchApiService);

  investigadores = signal<Investigador[]>([]);
  proyectos = signal<ProyectoInvestigacion[]>([]);
  publicaciones = signal<PublicacionCientifica[]>([]);
  cargando = signal<boolean>(true);
  menuAbierto = signal<boolean>(false);

  // Filtros Ciencia Accesible
  filtroActividad = signal<string>('Todos');
  categoriasActividad = ['Todos', 'Cursos gratuitos', 'Becas', 'Congresos', 'Eventos recreativos', 'Otras actividades'];
  actividades = [
    { categoria: 'Cursos gratuitos', titulo: 'Introducción a la divulgación científica', desc: 'Curso para aprender a comunicar contenidos científicos de forma clara y cercana.', detalle: 'Modalidad online asincrónica con certificación CCCh. Abierto a estudiantes y público general.' },
    { categoria: 'Becas', titulo: 'Becas para estudiantes investigadores', desc: 'Oportunidades de apoyo para estudiantes interesados en participar en investigación.', detalle: 'Apoyo de mentoría académica y financiamiento para pasantías en laboratorios asociados.' },
    { categoria: 'Congresos', titulo: 'Congreso de Jóvenes Investigadores', desc: 'Espacio para presentar proyectos, compartir ideas y conocer nuevos trabajos.', detalle: 'Convocatoria anual de ponencias y pósteres científicos a nivel nacional.' },
    { categoria: 'Eventos recreativos', titulo: 'Feria científica comunitaria', desc: 'Actividad abierta para acercar la ciencia a personas de todas las edades.', detalle: 'Talleres experimentales, observación astronómica y stands interactivos regionales.' },
    { categoria: 'Otras actividades', titulo: 'Charlas de ciencia para todos', desc: 'Conversaciones sobre temas científicos explicados de manera sencilla.', detalle: 'Ciclo mensual transmitido en vivo con ronda abierta de preguntas.' }
  ];
  actividadesFiltradas = computed(() => {
    const f = this.filtroActividad();
    return f === 'Todos' ? this.actividades : this.actividades.filter(a => a.categoria === f);
  });

  // Bolsa de trabajo
  busquedaEmpleo = signal<string>('');
  tipoEmpleo = signal<string>('Todos los tipos');
  ofertas = [
    { titulo: 'Ayudante de Investigación en Astroinformática', institucion: 'Observatorio / Red CCCh', tipo: 'Pasantía', ubicacion: 'Santiago / Remoto' },
    { titulo: 'Analista de Datos Ambientales y Energías Limpias', institucion: 'Centro de Innovación Energética', tipo: 'Jornada Completa', ubicacion: 'Antofagasta / Híbrido' }
  ];
  ofertasFiltradas = computed(() => {
    const q = this.busquedaEmpleo().trim().toLowerCase();
    const t = this.tipoEmpleo();
    return this.ofertas.filter(o =>
      (t === 'Todos los tipos' || o.tipo === t) &&
      (!q || o.titulo.toLowerCase().includes(q) || o.institucion.toLowerCase().includes(q))
    );
  });

  // Vitrina Visual (conectada a Proyectos y Publicaciones de PostgreSQL)
  filtroVitrina = signal<string>('Todo');

  // Foro de la Comunidad
  categoriaForo = signal<string>('General');
  categoriasForo = ['General', 'Investigación', 'Oportunidades', 'Colaboración', 'Eventos'];
  nuevoPostForo = '';
  postsForo = signal<{ categoria: string; autor: string; texto: string; fecha: string }[]>([]);

  // FAQ Acordeón
  faqAbierta = signal<number | null>(null);
  faqs = [
    { q: '¿Qué es la Comunidad Científica de Chile?', a: 'Es una red colaborativa que conecta a investigadores, estudiantes, profesionales y ciudadanía para impulsar y divulgar la ciencia en todo Chile.' },
    { q: '¿Quién puede unirse a la comunidad?', a: 'Investigadores acreditados, estudiantes de pregrado y postgrado, docentes, divulgadores y cualquier persona interesada en la ciencia.' },
    { q: '¿Cómo puedo publicar una oferta de trabajo?', a: 'Puedes enviarnos los detalles de la vacante o pasantía a través del formulario de contacto o desde tu perfil institucional.' },
    { q: '¿Cómo puedo publicar un proyecto en la vitrina?', a: 'Completa el formulario "Únete a la comunidad" indicando tu línea de investigación o proyecto para validarlo e incorporarlo en la Vitrina Visual.' },
    { q: '¿Tiene algún costo pertenecer a la comunidad?', a: 'No. La participación en la Comunidad Científica de Chile y el acceso a sus actividades de divulgación es completamente gratuito.' }
  ];

  // Formularios conectados a Django PostgreSQL (POST /api/solicitudes/)
  regionesChile = [
    'Arica y Parinacota', 'Tarapacá', 'Antofagasta', 'Atacama', 'Coquimbo',
    'Valparaíso', 'Metropolitana de Santiago', "O'Higgins", 'Maule', 'Ñuble',
    'Biobío', 'La Araucanía', 'Los Ríos', 'Los Lagos', 'Aysén', 'Magallanes'
  ];
  formUnete = { nombre: '', correo: '', area: '', region: '', bio: '' };
  estadoUnete = signal<{ ok: boolean; msg: string } | null>(null);
  enviandoUnete = signal<boolean>(false);

  formContacto = { nombre: '', email: '', mensaje: '' };
  estadoContacto = signal<{ ok: boolean; msg: string } | null>(null);
  enviandoContacto = signal<boolean>(false);

  // Modales (Iniciar Sesión y Ver más actividad)
  modalLoginAbierto = signal<boolean>(false);
  actividadSeleccionada = signal<{ categoria: string; titulo: string; desc: string; detalle: string } | null>(null);

  ngOnInit(): void {
    this.apiService.obtenerResumen().subscribe({
      next: (res) => {
        this.investigadores.set(res.investigadores);
        this.proyectos.set(res.proyectos);
        this.publicaciones.set(res.publicaciones);
        this.cargando.set(false);
      },
      error: () => this.cargando.set(false)
    });
  }

  irA(id: string): void {
    this.menuAbierto.set(false);
    document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
  }

  publicarEnForo(): void {
    if (!this.nuevoPostForo.trim()) return;
    this.postsForo.update(lista => [
      { categoria: this.categoriaForo(), autor: 'Miembro CCCh', texto: this.nuevoPostForo.trim(), fecha: 'Ahora' },
      ...lista
    ]);
    this.nuevoPostForo = '';
  }

  enviarSolicitudUnete(): void {
    if (!this.formUnete.nombre.trim() || !this.formUnete.correo.trim() || !this.formUnete.bio.trim()) {
      this.estadoUnete.set({ ok: false, msg: 'Completa nombre, correo y descripción antes de enviar.' });
      return;
    }
    this.enviandoUnete.set(true);
    this.apiService.enviarSolicitud({
      nombre_solicitante: this.formUnete.nombre,
      correo_contacto: this.formUnete.correo,
      institucion_origen: `${this.formUnete.area || 'General'} (${this.formUnete.region || 'Chile'})`,
      tipo_solicitud: 'INCORPORACION',
      mensaje: this.formUnete.bio
    }).subscribe({
      next: (r) => {
        this.estadoUnete.set({ ok: true, msg: r.mensaje });
        this.formUnete = { nombre: '', correo: '', area: '', region: '', bio: '' };
        this.enviandoUnete.set(false);
      },
      error: () => {
        this.estadoUnete.set({ ok: false, msg: 'No se pudo conectar con Django para guardar la solicitud.' });
        this.enviandoUnete.set(false);
      }
    });
  }

  enviarMensajeContacto(): void {
    if (!this.formContacto.nombre.trim() || !this.formContacto.email.trim() || !this.formContacto.mensaje.trim()) {
      this.estadoContacto.set({ ok: false, msg: 'Por favor completa todos los campos.' });
      return;
    }
    this.enviandoContacto.set(true);
    this.apiService.enviarSolicitud({
      nombre_solicitante: this.formContacto.nombre,
      correo_contacto: this.formContacto.email,
      institucion_origen: 'Contacto Web CCCh',
      tipo_solicitud: 'CONSULTA',
      mensaje: this.formContacto.mensaje
    }).subscribe({
      next: (r) => {
        this.estadoContacto.set({ ok: true, msg: r.mensaje });
        this.formContacto = { nombre: '', email: '', mensaje: '' };
        this.enviandoContacto.set(false);
      },
      error: () => {
        this.estadoContacto.set({ ok: false, msg: 'Error al registrar el mensaje en el servidor.' });
        this.enviandoContacto.set(false);
      }
    });
  }
}
