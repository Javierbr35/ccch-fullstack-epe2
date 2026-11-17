import { ComponentFixture, TestBed } from '@angular/core/testing';
import { InvestigadorCard } from './investigador-card';

describe('InvestigadorCard', () => {
  let component: InvestigadorCard;
  let fixture: ComponentFixture<InvestigadorCard>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [InvestigadorCard],
    }).compileComponents();

    fixture = TestBed.createComponent(InvestigadorCard);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
