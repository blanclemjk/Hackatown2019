import { injectable, } from "inversify";
import * as http from "http";
import * as Io from "socket.io";
//import * as request from "request-promise-native";


@injectable()
export class SocketService {
    private socketServer: SocketIO.Server;
    public space: Map<SocketIO.Socket, number>;
    

    public createServer(server: http.Server): void {
        console.log("ALLO");
        this.space = new Map<SocketIO.Socket, number>();
        console.log(this.space);
        setInterval(() => {this.updateAllParking();}, 3000);
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
                    this.space.set(socket, parkings[0]);
                    socket.emit("destination", parkings[0]);
                } else {
                    socket.emit("destination", -1);
                }   
            }
            ).catch();
        });
    }

    private async updateParking(socket: SocketIO.Socket): Promise<void> {
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
    }

    private updateAllParking(): void {
        console.log(this.space)
        if(this.space.size > 0) {
            this.space.forEach((value: number, key: SocketIO.Socket) => {
            this.updateParking(key).then().catch();
        });
        }
        
        console.log("CRON JOB\n");
    }

    private async requestParking(): Promise<number[]> {
        const test: number[] = [3];
        return /*request("localhost:3001/parking");*/ test;
    }

}
