import { ComponentFixture, TestBed } from '@angular/core/testing';
import { CienciaAccesible } from './ciencia-accesible';

describe('CienciaAccesible', () => {
  let component: CienciaAccesible;
  let fixture: ComponentFixture<CienciaAccesible>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CienciaAccesible],
    }).compileComponents();

    fixture = TestBed.createComponent(CienciaAccesible);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
