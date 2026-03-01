import http from "k6/http";
import { check } from "k6";
import { BASE_URL, USER, OPTIONS_UNIT } from "./config.js";

export const options = OPTIONS_UNIT;

export default function () {
  // 1️⃣ REGISTER (idempotent-friendly)
  http.post(
    `${BASE_URL}/api/auth/register`,
    JSON.stringify({
      name: "k6 user",
      email: USER.email,
      password: USER.password,
    }),
    { headers: { "Content-Type": "application/json" } }
  );

  // 2️⃣ LOGIN
  const res = http.post(
    `${BASE_URL}/api/auth/login`,
    JSON.stringify(USER),
    { headers: { "Content-Type": "application/json" } }
  );

  console.log("STATUS:", res.status);
  console.log("HEADERS:", JSON.stringify(res.headers));
  console.log("BODY:", res.body);

  check(res, {
    "login success (2xx)": (r) => r.status >= 200 && r.status < 300,
    "session cookie set": (r) =>
      r.headers["Set-Cookie"] !== undefined,
  });
}