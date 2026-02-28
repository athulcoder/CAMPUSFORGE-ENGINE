import http from "k6/http";
import { check } from "k6";
import { uuidv4 } from "https://jslib.k6.io/k6-utils/1.4.0/index.js";

export default function () {
  const email = `user_${uuidv4()}@test.com`;

  // register
  http.post(
    "http://localhost:8080/api/auth/register",
    JSON.stringify({
      name: "k6 user",
      email,
      password: "123456",
    }),
    { headers: { "Content-Type": "application/json" } }
  );

  // login (cookie stored)
  const login = http.post(
    "http://localhost:8080/api/auth/login",
    JSON.stringify({ email, password: "123456" }),
    { headers: { "Content-Type": "application/json" } }
  );

  check(login, { "login ok": (r) => r.status === 200 });

  // upload resume
  const file = open("./resume.pdf", "b");
  http.post("http://localhost:8080/api/resume/upload", {
    file: http.file(file, "resume.pdf"),
  });
}