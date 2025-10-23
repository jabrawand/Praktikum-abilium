import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AddTaskComponent } from './pages/add-task/add-task.component';
import { NotFoundComponent } from './pages/not-found/not-found.component';
import { TaskDetailsComponent } from './task-details/task-details.component';

export const routes: Routes = [
    {path: "", component: HomeComponent},
    {path: "add-task", component: AddTaskComponent},
    {path: "**", component: NotFoundComponent},
    {path: "task/:id", component: TaskDetailsComponent}
];
