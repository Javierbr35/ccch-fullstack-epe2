import { Component, input } from '@angular/core';
import { Investigador } from '../../services/ccch-api.service';
@Component({ selector: 'app-investigador-card', imports: [], templateUrl: './investigador-card.html', styleUrl: './investigador-card.css' })
export class InvestigadorCard {
  investigador = input.required<Investigador>();
  obtenerIniciales(n: string): string { return n.replace(/^(Dr\.|Dra\.|Mg\.|Ing\.)\s*/i, '').split(' ').slice(0, 2).map((p) => p[0]).join('').toUpperCase(); }
}
