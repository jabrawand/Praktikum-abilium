import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-add-task',
  imports: [],
  templateUrl: './add-task.component.html',
  styleUrl: './add-task.component.css'
})
export class AddTaskComponent {
  constructor(private router: Router) {}
  addTask() {
    alert('Task Added Successfully');
    this.router.navigate(['/'])
  }

}
