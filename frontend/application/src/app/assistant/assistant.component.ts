import { Component } from '@angular/core';

@Component({
  selector: 'app-assistant',
  templateUrl: './assistant.component.html',
  styleUrl: './assistant.component.css'
})
export class AssistantComponent {
  assistantPicturePath: string = '/assets/veles_assist.png';
  selectedHint: { type: string, text: string } | null = null;
  hints: { type: string, text: string, showText: boolean }[] = [
    { type: 'structure', text: 'Hint 1: This is an structure hint' , showText: false},
    { type: 'validation', text: 'Hint 2: This is a validation hint' , showText: false},
    { type: 'error', text: 'Hint 3: This is a error hint' , showText: false},
    { type: 'complexity', text: 'Hint 4: This is a complexity hint' , showText: false},
    { type: 'structure', text: 'Hint 1: This is an structure hint' , showText: false},
    { type: 'validation', text: 'Hint 2: This is a validation hint' , showText: false},
    { type: 'error', text: 'Hint 3: This is a error hint' , showText: false},
    { type: 'complexity', text: 'Hint 4: This is a complexity hint' , showText: false}
  ];

  changePicturePath(newPath: string) {
    this.assistantPicturePath = newPath;
  }

  filterHintsByType(type: string): { type: string, text: string , showText:boolean}[] {
    return this.hints.filter(hint => hint.type === type);
  }

  showHint(hint: { type: string, text: string, showText: boolean }) {
    // hint.showText = !hint.showText;
    this.selectedHint = hint;
    switch (hint.type) {
      case 'structure':
        this.changePicturePath('/assets/vesna_assist.png');
        break;
      case 'validation':
        this.changePicturePath('/assets/vid_assist.png');
        break;
      case 'error':
        this.changePicturePath('/assets/vid_assist.png');
        break;
      case 'complexity':
        this.changePicturePath('/assets/veles_assist.png');
        break;
    }
  }
}
