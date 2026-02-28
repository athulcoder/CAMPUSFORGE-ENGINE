import http from "k6/http";
import { check } from "k6";
import { BASE_URL, USER, OPTIONS_LOAD } from "./config.js";

export const options = OPTIONS_LOAD;

export default function () {
  // login first (cookie stored)
  http.post(
    `${BASE_URL}/api/auth/login`,
    JSON.stringify(USER),
    { headers: { "Content-Type": "application/json" } }
  );

  const file = open("./resume.pdf", "b");

  const res = http.post(
    `${BASE_URL}/api/resume/upload`,
    { file: http.file(file, "resume.pdf") }
  );

  check(res, {
    "resume uploaded": (r) =>
      r.status === 200 || r.status === 201,
  });
}