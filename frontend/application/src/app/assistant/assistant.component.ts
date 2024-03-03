import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { EventEmitterService } from '../event-emitter.service';

@Component({
  selector: 'app-assistant',
  templateUrl: './assistant.component.html',
  styleUrl: './assistant.component.css'
})
export class AssistantComponent implements OnInit{
  assistantPicturePath: string = '/assets/veles_assist.png';
  selectedHint: { type: string, text: string } | null = null;
  hints : any;

  constructor(private eventEmitterDataService: EventEmitterService,
    private cdr: ChangeDetectorRef) { }

  ngOnInit(): void {
    this.eventEmitterDataService.hintsReceived.subscribe((response: any) => {
      console.log('Hints received:', response);
      let flattenedArray = response.hints.flatMap((innerArray: any[], submission: any) =>
        innerArray.map(obj => ({ ...obj, submission }))
      );
      console.log(flattenedArray);
      this.hints = flattenedArray;
      this.cdr.detectChanges();
    });
  }

  changePicturePath(newPath: string) {
    this.assistantPicturePath = newPath;
  }

  // filterHintsByType(type: string): { type: string, text: string , showText:boolean}[] {
  //   return this.hints.filter(hint => hint.type === type);
  // }

  showHint(hint: { type: string, text: string, showText: boolean }) {
    // hint.showText = !hint.showText;
    this.selectedHint = hint;
    switch (hint.type) {
      case 'STRUCTURE':
        this.changePicturePath('/assets/vesna_assist.png');
        break;
      case 'VALIDATION':
        this.changePicturePath('/assets/vid_assist.png');
        break;
      case 'ERROR':
        this.changePicturePath('/assets/vid_assist.png');
        break;
      case 'COMPLEXITY':
        this.changePicturePath('/assets/veles_assist.png');
        break;
    }
  }
}
