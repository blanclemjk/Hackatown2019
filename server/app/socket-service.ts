import { injectable, } from "inversify";
import * as http from "http";
import * as Io from "socket.io";
//import * as request from "request-promise-native";


@injectable()
export class SocketService {
    private socketServer: SocketIO.Server;
    public space: Map<SocketIO.Socket, number>;
    

    public createServer(server: http.Server): void {
        this.space = new Map<SocketIO.Socket, number>();
        this.socketServer = Io(server);
        this.socketServer.on("connection", (socket: SocketIO.Socket) => {
            this.space.set(socket, -1);
            socket.emit("connection successfull");
            this.initParkingRequest(socket);
            this.onDisconnect(socket);
        } );


    }
   private onDisconnect(socket: SocketIO.Socket): void {
        socket.on("disconnect", () => {
            this.space.delete(socket);
        });
    }

    
    private initParkingRequest(socket: SocketIO.Socket): void {
        socket.on("parking", () => {
            this.requestParking().then((parkings: number[]) => {
                if(parkings.length > 0) {
                this.space.forEach((value: number, key: SocketIO.Socket) => {
                    let stillFree: Boolean = false; 
                        for(let freeSpace of parkings) {
                            if(value === freeSpace) {
                                stillFree = true;
                                break;
                            }
                        }
                        if(!stillFree) {
                            this.space.set(socket, parkings[0]);
                            socket.emit("destination", parkings[0]);
                        }
                });
                } else {
                    socket.emit("destination", -1);
                }
            }   
            ).catch();
            
        });
    }

    private async requestParking(): Promise<number[]> {
        const test: number[] = [3];
        return /*request("localhost:3001/parking");*/ test;
    }

}
