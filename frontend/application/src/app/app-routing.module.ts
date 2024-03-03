import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AssignmentComponent } from './assignment/assignment.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  {path: 'assignment/:id', component: AssignmentComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
