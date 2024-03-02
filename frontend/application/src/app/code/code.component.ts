import { Component } from '@angular/core';

@Component({
  selector: 'app-code',
  templateUrl: './code.component.html',
  styleUrl: './code.component.css'
})
export class CodeComponent {

  selectedLanguage: string = 'typescript'; //default language

  editorOptions = {theme: 'vs-dark', language: 'typescript'};
  code: string= 'function x() {\nconsole.log("Hello world!");\n}';

  changeLanguage() {
    this.editorOptions.language = this.selectedLanguage;
  }
}
