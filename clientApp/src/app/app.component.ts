import { Component } from '@angular/core';
import { SocketService } from './socket.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.less']
})
export class AppComponent {
  constructor(private socket: SocketService) {}
  title = 'clientApp';
  private requested = false;

  request() {
    setTimeout(_ => {this.requested = true; }, 500);
  }
}
