import { Component } from '@angular/core';


import {HEROES} from '../mock-heroes';
import { NgFor, NgIf, UpperCasePipe } from '@angular/common';
import { FormsModule } from '@angular/forms';



@Component({
  /* standalone: true, Frage: wozu ist standalone und warum funktioniert dies bei mir nicht? */
  selector: 'app-heroes',
  templateUrl: './heroes.component.html',
  styleUrl: './heroes.component.css',
  imports: [
    FormsModule,
    NgIf,
    NgFor,
    UpperCasePipe,
  ]
  
})
export class HeroesComponent {
 
 heroes = HEROES;

}
