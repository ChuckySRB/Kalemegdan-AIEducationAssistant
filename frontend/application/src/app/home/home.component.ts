import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

  constructor(private router: Router) { }

  tasks: string[] = ['Task 1', 'Task 2', 'Task 3'];

  navigateToAssignment(task: string) {
    // this.taskService.selectTask(task);
    this.router.navigate(['/assignment']);
  }
}
