import { Injectable } from '@angular/core';
import { Message } from './message';

@Injectable({
  providedIn: 'root'
})
export class MessageService {
  messages: Message[] = [];

  //add a new Message to messages from text and class parameters
  add(cssClass: string, message: string) {
    this.messages.push({
      cssClass: cssClass,
      message: message
    });
  }

  clear() {
    this.messages = [];
  }

  constructor() { }
}
