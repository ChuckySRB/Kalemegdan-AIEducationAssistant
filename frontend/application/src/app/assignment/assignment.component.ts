import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AssignmentService } from '../assignment.service';

@Component({
  selector: 'app-assignment',
  templateUrl: './assignment.component.html',
  styleUrl: './assignment.component.css'
})
export class AssignmentComponent implements OnInit{

  taskId!: number;
  taskName: any;
  taskDesc: any;

  constructor(private route: ActivatedRoute, private assignmentService: AssignmentService) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.taskId = +params['id'];
      this.loadTask();
    });
  }

  loadTask(): void {
    this.assignmentService.getAssignmentById(this.taskId).subscribe(
      (response: any) => {
        // console.log(response);
        this.taskName = response.task_name;
        this.taskDesc = response.task_desc;
      },
      (error) => {
        console.error('Error fetching task:', error);
      }
    );
  }
}
