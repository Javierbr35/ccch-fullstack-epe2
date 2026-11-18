import { Component, input } from '@angular/core';
import { PublicacionCientifica } from '../../services/ccch-api.service';
@Component({ selector: 'app-publicacion-card', imports: [], templateUrl: './publicacion-card.html', styleUrl: './publicacion-card.css' })
export class PublicacionCard {
  publicacion = input.required<PublicacionCientifica>();
}
