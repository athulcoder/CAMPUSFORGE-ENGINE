import http from "k6/http";
import { check } from "k6";
import { BASE_URL, USER, OPTIONS_UNIT } from "./config.js";

export const options = OPTIONS_UNIT;

export default function () {
  const res = http.post(
    `${BASE_URL}/api/auth/login`,
    JSON.stringify(USER),
    { headers: { "Content-Type": "application/json" } }
  );

  check(res, {
    "login success": (r) => r.status === 200,
    "session cookie set": (r) =>
      r.headers["Set-Cookie"] !== undefined,
  });
}