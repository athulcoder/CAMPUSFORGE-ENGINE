import http from "k6/http";
import { check } from "k6";
import { BASE_URL, USER, OPTIONS_LOAD } from "./config.js";

export const options = OPTIONS_LOAD;

export default function () {
  http.post(
    `${BASE_URL}/api/auth/login`,
    JSON.stringify(USER),
    { headers: { "Content-Type": "application/json" } }
  );

  const res = http.get(
    `${BASE_URL}/api/candidate?role=React Developer`
  );

  check(res, {
    "status 200": (r) => r.status === 200,
    "redis fast": (r) => r.timings.duration < 200,
  });
}