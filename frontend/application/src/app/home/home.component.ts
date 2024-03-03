import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AssignmentService } from '../assignment.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit{

  constructor(private router: Router, private assignmentService: AssignmentService) { }

  ngOnInit(): void {
    this.assignmentService.getAllAssignments().subscribe((data: any) => {
      // console.log(data);
      this.tasks = data.tasks;
      // console.log(this.tasks);
    });
  }
  // tasks: string[] = ['Task 1', 'Task 2', 'Task 3'];
  tasks: any[] = [];

  navigateToAssignment(task: any): void {
    this.router.navigate(['/assignment', task.idT]);
  }
}
