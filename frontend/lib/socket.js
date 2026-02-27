import { io } from "socket.io-client";

export const socket = io("http://localhost:8080", {
  transports: ["websocket", "polling"],
  withCredentials: true,
});


socket.on("connect", () => {
    console.log("🟢 CONNECTED", socket.id);
    socket.emit("ping_test", { msg: "hello" });
  });

  socket.on("disconnect", () => {
    console.log("🔴 DISCONNECTED");
  });