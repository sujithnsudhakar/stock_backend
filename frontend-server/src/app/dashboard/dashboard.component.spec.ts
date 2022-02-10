import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DashboardComponent } from './dashboard.component';

describe('DashboardComponent', () => {
  let component: DashboardComponent;
  let fixture: ComponentFixture<DashboardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DashboardComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should call onSubmit() and print console.log', () => {
    component.onSubmit();
    expect(console.log).toHaveBeenCalledWith('Submit button has been clicked!');
  });

  it('Prediction date is undefined on ngOnInit and is set from the form on submit', () => {
    expect(component.predictionDate).not.toBeDefined;
    component.onSubmit();
    expect(component.predictionDate).toHaveBeenCalledOnceWith(component.onSubmit());
    expect(component.predictionDate).toBeDefined;
  });

  it('Company name is undefined on ngOnInit and is set from the form on submit', () => {
    expect(component.companyName).not.toBeDefined;
    component.onSubmit();
    expect(component.companyName).toHaveBeenCalledOnceWith(component.onSubmit());
    expect(component.companyName).toBeDefined;
  });
  
  it('should Fetch all company names on getCompanyList()', () => {
    //TODO 
  });
  
});
