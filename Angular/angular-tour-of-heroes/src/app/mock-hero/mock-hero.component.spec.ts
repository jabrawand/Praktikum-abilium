import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MockHeroComponent } from './mock-hero.component';

describe('MockHeroComponent', () => {
  let component: MockHeroComponent;
  let fixture: ComponentFixture<MockHeroComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [MockHeroComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(MockHeroComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
