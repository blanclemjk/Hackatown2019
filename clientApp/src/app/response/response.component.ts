import { Component, OnInit } from '@angular/core';
import { SocketService } from '../socket.service';

@Component({
  selector: 'app-response',
  templateUrl: './response.component.html',
  styleUrls: ['./response.component.less']
})
export class ResponseComponent implements OnInit {


  constructor(private socket: SocketService) { }

  ngOnInit() {
  }

}
