import { Component } from '@angular/core';
import { Router, RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [
    RouterOutlet,
    RouterLink,
    RouterLinkActive
    ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  id = 1
  title = 'angular-routing-app';
  constructor(private router: Router) {}

  viewDetails() {
    this.router.navigate(['task', this.id])
  }
}
