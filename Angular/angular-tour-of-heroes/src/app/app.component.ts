import { Component } from '@angular/core';
/* Frage: Im Beispiel steht standalone: true; wenn ich dies einfüge, funktioniert ng serve --open nicht mehr?!*/
@Component({
  selector: 'app-root', 
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Tour of Heroes';
}
