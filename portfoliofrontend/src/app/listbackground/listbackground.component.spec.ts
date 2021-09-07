import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListbackgroundComponent } from './listbackground.component';

describe('ListbackgroundComponent', () => {
  let component: ListbackgroundComponent;
  let fixture: ComponentFixture<ListbackgroundComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListbackgroundComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListbackgroundComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
