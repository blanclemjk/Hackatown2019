"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
require("reflect-metadata");
const inversify_1 = require("inversify");
const types_1 = require("./types");
const server_1 = require("./server");
const app_1 = require("./app");
const container = new inversify_1.Container();
exports.container = container;
container.bind(types_1.default.Server).to(server_1.Server);
container.bind(types_1.default.Application).to(app_1.Application);
//# sourceMappingURL=inversify.config.js.map