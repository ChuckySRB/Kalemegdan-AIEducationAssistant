import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AssignmentService {
  private url = 'http://localhost:3000/assignments';

  constructor(private http:HttpClient) { }

  getAllAssignments() {
    return this.http.get(`${this.url}/get_all`);
  }

  getAssignmentById(id: number) {
    return this.http.get(`${this.url}/get_assignment/${id}`);
  }

  sendAttempt(attempt: any) {
    return this.http.post(`${this.url}/send_attempt`, attempt);
  }
}
