import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrinosComponent } from './trinos.component';

describe('TrinosComponent', () => {
  let component: TrinosComponent;
  let fixture: ComponentFixture<TrinosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrinosComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TrinosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
