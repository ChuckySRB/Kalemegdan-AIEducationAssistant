import { Injectable } from '@angular/core';
import * as monaco from 'monaco-editor';

@Injectable({
  providedIn: 'root'
})
export class EditorService {
  private editor: monaco.editor.IStandaloneCodeEditor | undefined;

  constructor() {
  }

  setEditor(editor: monaco.editor.IStandaloneCodeEditor) {
    this.editor = editor;

    // console.log('Editor set');
  }

  setLanguage(language: string) {
    if (this.editor) {
      monaco.editor.setModelLanguage(this.editor.getModel()!, language);
      // console.log('Language changed to ' + language);
    }
    // console.log('No editor found');
  }
}
