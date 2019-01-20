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
const express = require("express");
//import * as path from "path";
const logger = require("morgan");
const cookieParser = require("cookie-parser");
const bodyParser = require("body-parser");
const cors = require("cors");
//import Types from "./types";
const inversify_1 = require("inversify");
//import  { RouterApi } from "./routers/router-api"
let Application = class Application {
    constructor() {
        this.internalError = 500;
        this.app = express();
        this.config();
        this.routes();
    }
    config() {
        // Middlewares configuration
        this.app.use(logger("dev"));
        this.app.use(bodyParser.json());
        this.app.use(bodyParser.urlencoded({ extended: true }));
        this.app.use(cookieParser());
        //this.app.use(express.static(path.join(__dirname, "../client")));
        //this.app.use(express.static(path.join(__dirname, 'public')));
        this.app.use(cors());
    }
    routes() {
        this.app.get("/parking", (req, res) => res.send("parking"));
        this.errorHandeling();
    }
    errorHandeling() {
        // Gestion des erreurs
        this.app.use((req, res, next) => {
            const err = new Error("Not Found");
            next(err);
        });
        // development error handler
        // will print stacktrace
        if (this.app.get("env") === "development") {
            // tslint:disable-next-line:no-any
            this.app.use((err, req, res, next) => {
                res.status(err.status || this.internalError);
                res.send({
                    message: err.message,
                    error: err
                });
            });
        }
        // production error handler
        // no stacktraces leaked to user (in production env only)
        // tslint:disable-next-line:no-any
        this.app.use((err, req, res, next) => {
            res.status(err.status || this.internalError);
            res.send({
                message: err.message,
                error: {}
            });
        });
    }
};
Application = __decorate([
    inversify_1.injectable(),
    __metadata("design:paramtypes", [])
], Application);
exports.Application = Application;
//# sourceMappingURL=app.js.map