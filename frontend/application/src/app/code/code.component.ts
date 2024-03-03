import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';
import { EditorService } from '../editor.service';
import * as monaco from 'monaco-editor';

@Component({
  selector: 'app-code',
  templateUrl: './code.component.html',
  styleUrl: './code.component.css'
})
export class CodeComponent implements AfterViewInit{
  @ViewChild('editor') editor: any;

  constructor(private editorService:EditorService) {}

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
}
