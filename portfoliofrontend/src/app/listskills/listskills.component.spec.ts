import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListskillsComponent } from './listskills.component';

describe('ListskillsComponent', () => {
  let component: ListskillsComponent;
  let fixture: ComponentFixture<ListskillsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListskillsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListskillsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
