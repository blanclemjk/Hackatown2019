"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
Object.defineProperty(exports, "__esModule", { value: true });
const inversify_1 = require("inversify");
const Io = require("socket.io");
//import * as Event from "../../../common/events/events";
//import { Room } from "../../../common/interface/room-interface";
//import * as request from "request-promise-native";
let ServiceMultiplayer = class ServiceMultiplayer {
    createServer(server) {
        this.socketServer = Io(server);
    }
};
ServiceMultiplayer = __decorate([
    inversify_1.injectable()
], ServiceMultiplayer);
exports.ServiceMultiplayer = ServiceMultiplayer;
//# sourceMappingURL=socket-service.js.map