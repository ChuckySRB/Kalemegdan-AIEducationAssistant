import { EventEmitter, Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EventEmitterService {

  hintsReceived = new EventEmitter<any>();

  constructor() { }

  receiveHints(data: any): void {
    // Emit an event with the updated data
    this.hintsReceived.emit(data);
  }
}
