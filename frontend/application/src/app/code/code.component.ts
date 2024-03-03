import { AfterViewInit, Component, Input, OnInit, ViewChild } from '@angular/core';
import { EditorService } from '../editor.service';
import * as monaco from 'monaco-editor';
import { AssignmentService } from '../assignment.service';
import { EventEmitterService } from '../event-emitter.service';

@Component({
  selector: 'app-code',
  templateUrl: './code.component.html',
  styleUrl: './code.component.css'
})
export class CodeComponent implements AfterViewInit{
  @ViewChild('editor') editor: any;
  @Input() taskId: number | undefined;

  constructor(private editorService:EditorService, private assignmentService: AssignmentService, private eventEmitter: EventEmitterService) {}

  selectedLanguage: string = 'typescript'; //default language

  editorOptions = {theme: 'vs-dark', language: 'typescript'};
  code: string= 'function x() {\nconsole.log("Hello world!");\n}';

  ngAfterViewInit() {
    this.editorService.setEditor(this.editor.editor);
  }

  changeLanguage() {
    // this.editorService.setLanguage(this.selectedLanguage);
    this.editorOptions = {theme: 'vs-dark', language: this.selectedLanguage};
  }

  sendAttempt(){
    const attempt = {
      idT: this.taskId,
      time: new Date().toISOString(),
      code: this.code
    }

    this.assignmentService.sendAttempt(attempt).subscribe(
      (response) => {
        console.log('Attempt sent:', response);
        this.eventEmitter.receiveHints(response);
      },
      (error) => {
        console.error('Error sending attempt:', error);
      }
    );
  }
}
