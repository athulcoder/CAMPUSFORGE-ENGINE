import http from "k6/http";
import { check } from "k6";
import { BASE_URL, USER, OPTIONS_LOAD } from "./config.js";

const RESUME_ID =
  "a4ef69e4-8c00-40b5-b854-46e8d9571ef6";

export const options = OPTIONS_LOAD;

export default function () {
  http.post(
    `${BASE_URL}/api/auth/login`,
    JSON.stringify(USER),
    { headers: { "Content-Type": "application/json" } }
  );

  const res = http.get(
    `${BASE_URL}/api/candidate/${RESUME_ID}`
  );

  check(res, {
    "details ok": (r) => r.status === 200,
  });
}