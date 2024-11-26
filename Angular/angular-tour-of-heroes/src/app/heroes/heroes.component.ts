import { Component } from '@angular/core';


import {HEROES} from '../mock-heroes';
import { NgFor } from '@angular/common';



@Component({
  /* standalone: true, Frage: wozu ist standalone und warum funktioniert dies bei mir nicht? */
  selector: 'app-heroes',
  templateUrl: './heroes.component.html',
  styleUrl: './heroes.component.css',
  imports: [
    NgFor,
  ]
  
})
export class HeroesComponent {
 
 heroes = HEROES;

}
