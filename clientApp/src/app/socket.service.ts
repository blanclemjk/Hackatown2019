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

  public hasDest(): boolean {
    return this.dest !== undefined;
  }

  constructor(private socket: Socket) {
    socket.on('destination', (newDest: number) => {
      if (!this.dest) {
        // show popop?
      }
      this.dest = newDest;
    });
    setTimeout(_ => {socket.emit('connection'); }, 1000);
  }
}
