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
        console.log(this.space);
        //setInterval(() => {this.updateAllParking();}, 3000);
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
                this.space.set(socket, -1);
        });
    }

    private async updateParking(socket: SocketIO.Socket, parkings: number[]): Promise<void> {
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

    private updateAllParking(parkings: number[]): void {
        if(this.space.size > 0) {
            this.space.forEach((value: number, key: SocketIO.Socket) => {
            this.updateParking(key, parkings).then().catch();
        });
        }
    }

    public updateParkings(req: any, res: any) {
        console.log(req.body);
        this.updateAllParking(req.body.parkings);
        res.json("ok");
    }

}
