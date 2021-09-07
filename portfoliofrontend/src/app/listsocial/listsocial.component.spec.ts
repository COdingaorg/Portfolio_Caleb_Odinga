import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListsocialComponent } from './listsocial.component';

describe('ListsocialComponent', () => {
  let component: ListsocialComponent;
  let fixture: ComponentFixture<ListsocialComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListsocialComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListsocialComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
