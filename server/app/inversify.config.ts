import "reflect-metadata";
import { Container } from "inversify";
import Types from "./types";
import { Server } from "./server";
import { Application } from "./app";



const container: Container = new Container();

container.bind(Types.Server).to(Server);
container.bind(Types.Application).to(Application);


export { container };
