import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';

@Injectable({
  providedIn: 'root'
})
export class SocketService {

  private dest: number;
  public getDest(): number {
    return this.dest;
  }

  constructor(private socket: Socket) {
    socket.on('destination', (newDest: number) => {
      if (!this.dest) {
        // show popop?
      }
      this.dest = newDest;
    });
    socket.emit('connection');
  }
}
