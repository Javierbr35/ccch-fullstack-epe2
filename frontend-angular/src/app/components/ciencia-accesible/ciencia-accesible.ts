import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-ciencia-accesible',
  imports: [],
  templateUrl: './ciencia-accesible.html',
  styleUrl: './ciencia-accesible.css',
})
export class CienciaAccesible {
  recursoActivo = signal<number | null>(0);
  recursos = [
    { titulo: 'Charlas Científicas en Establecimientos Educacionales', categoria: 'Vinculación Escolar', descripcion: 'Investigadores de la red CCCh visitan liceos y colegios a lo largo de Chile para acercar la astronomía, biotecnología y energías limpias.', detalle: 'Modalidad presencial y streaming nacional gratuita con material didáctico descargable para docentes.' },
    { titulo: 'Repositorio Abierto de Datos y Metodologías', categoria: 'Ciencia Abierta', descripcion: 'Acceso libre a conjuntos de datos experimentales, cuadernos Jupyter y protocolos reproducibles generados por equipos chilenos.', detalle: 'Licenciamiento Creative Commons para fomentar la colaboración interuniversitaria.' },
    { titulo: 'Boletín de Divulgación para Público General', categoria: 'Cultura Científica', descripcion: 'Síntesis mensuales en lenguaje claro sobre los hallazgos más relevantes publicados en revistas indexadas desde Chile.', detalle: 'Editado por el comité de comunicación científica de la CCCh.' }
  ];
  alternarDetalle(indice: number): void { this.recursoActivo.update((actual) => (actual === indice ? null : indice)); }
}
