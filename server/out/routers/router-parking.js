"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
Object.defineProperty(exports, "__esModule", { value: true });
const inversify_1 = require("inversify");
const express_1 = require("express");
//import Types from "../types";
let RouterParking = class RouterParking {
    constructor() { }
    get routes() {
        const router = express_1.Router();
        /*
        router.get(
                "/words/:constraint",
                (req: Request, res: Response ) => this.lexicalService.getAllWords(req.params.constraint, req.query.rarety, res));
        router.get(
                "/definition/:word",
                (req: Request, res: Response ) => this.lexicalService.getWordDefinitions(req.params.word, req.query.difficulty, res));
                */
        return router;
    }
};
RouterParking = __decorate([
    inversify_1.injectable(),
    __metadata("design:paramtypes", [])
], RouterParking);
exports.RouterParking = RouterParking;
//# sourceMappingURL=router-parking.js.map