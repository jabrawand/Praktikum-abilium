import { Component } from '@angular/core';

import { HEROES } from '../mock-heroes';
import { NgFor } from '@angular/common';


@Component({
  standalone: true,
  imports: [
    NgFor,
  ],
  selector: 'app-heroes',
  templateUrl: './heroes.component.html',
  styleUrls: ['./heroes.component.css']
})
export class HeroesComponent {
  heroes = HEROES;
}
