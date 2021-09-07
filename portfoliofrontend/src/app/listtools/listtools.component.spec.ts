import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListtoolsComponent } from './listtools.component';

describe('ListtoolsComponent', () => {
  let component: ListtoolsComponent;
  let fixture: ComponentFixture<ListtoolsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListtoolsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListtoolsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
