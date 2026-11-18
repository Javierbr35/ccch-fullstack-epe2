import { Component, input } from '@angular/core';
import { DecimalPipe } from '@angular/common';
import { ProyectoInvestigacion } from '../../services/ccch-api.service';
@Component({ selector: 'app-proyecto-card', imports: [DecimalPipe], templateUrl: './proyecto-card.html', styleUrl: './proyecto-card.css' })
export class ProyectoCard {
  proyecto = input.required<ProyectoInvestigacion>();
}
