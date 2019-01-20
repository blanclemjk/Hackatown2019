import { injectable, } from "inversify";
import * as http from "http";
import * as Io from "socket.io";
//import * as Event from "../../../common/events/events";
//import { Room } from "../../../common/interface/room-interface";
import * as request from "request-promise-native";

@injectable()
export class ServiceMultiplayer {
    private socketServer: SocketIO.Server;
    

    public createServer(server: http.Server): void {
        this.socketServer = Io(server);
        this.socketServer.on("connection", (socket: SocketIO.Socket) => {

            socket.emit("connection successfull");
            this.initParkingRequest(socket);
        } );
    }

    
    private initParkingRequest(socket: SocketIO.Socket): void {
        socket.on("parking", () => {
            this.requestParking().then((parkings: string[]) => {
                
            }
            ).catch();
        });
    }

    public async requestParking(): Promise<string[]> {
        return request("localhost:3001/parking");
    }

}
