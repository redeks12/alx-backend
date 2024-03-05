import { createClient } from "redis";
const client = new createClient();
client
  .on("connection", (val) => {
    console.log("Redis client connected to the server");
  })
  .on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });
