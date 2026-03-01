import http, { cookieJar } from "k6/http";
import { check, group, sleep } from "k6";
import { BASE_URL, OPTIONS_20_USERS } from "./config.js";

export const options = OPTIONS_20_USERS;


/* ================================
   SETUP – REGISTER ONCE
==================================*/
export function setup() {
  const email = `k6_${Date.now()}@test.com`;

  const res = http.post(
    `${BASE_URL}/api/auth/register`,
    JSON.stringify({
      name: "K6 Recruiter",
      email,
      password: "123456",
    }),
    {
      headers: { "Content-Type": "application/json" },
      tags: { api: "register" },
    }
  );

  check(res, {
    "register ok": (r) => r.status === 200 || r.status === 201,
  });

  return { email };
}

/* ================================
   MAIN TEST – 20 USERS
==================================*/
export default function (data) {
  const jar = cookieJar();

  /* ---------- LOGIN (ONCE PER VU) ---------- */
  if (!jar.cookiesForURL(BASE_URL).sessionId) {
    const res = http.post(
      `${BASE_URL}/api/auth/login`,
      JSON.stringify({
        email: data.email,
        password: "123456",
      }),
      {
        headers: { "Content-Type": "application/json" },
        tags: { api: "login" },
      }
    );

    check(res, {
      "login success": (r) => r.status === 200,
    });
  }

  sleep(Math.random());

  /* ---------- CANDIDATE (ALL) – REDIS ---------- */
  let resumeId = null;

  group("/api/candidate (all)", () => {
    const res = http.get(`${BASE_URL}/api/candidate`, {
      tags: { api: "candidate_all" },
    });

    check(res, {
      "candidate list ok": (r) => r.status === 200,
    });

    const list = res.json();
    if (Array.isArray(list) && list.length > 0) {
      resumeId =
        list[Math.floor(Math.random() * list.length)].id;
    }
  });

  sleep(Math.random());

  /* ---------- CANDIDATE (ROLE) – REDIS ---------- */
  group("/api/candidate?role", () => {
    const res = http.get(
      `${BASE_URL}/api/candidate?role=React&Developer`,
      { tags: { api: "candidate_role" } }
    );

    check(res, {
      "role fetch ok": (r) => r.status === 200,
    });
  });

  sleep(Math.random());

  /* ---------- CANDIDATE BY ID – DB ---------- */
  if (resumeId) {
    group("/api/candidate/:id", () => {
      const res = http.get(
        `${BASE_URL}/api/candidate/${resumeId}`,
        { tags: { api: "candidate_id" } }
      );

      check(res, {
        "candidate detail ok": (r) => r.status === 200,
      });
    });
  }

  sleep(Math.random());

  /* ---------- RESUME UPLOAD (BURSTY) ---------- */
  if (Math.random() < 0.2) {
    group("/api/resume/upload", () => {
      const file = open("./resume.pdf", "b");

      const res = http.post(
        `${BASE_URL}/api/resume/upload`,
        {
          file: http.file(file, "resume.pdf"),
        },
        { tags: { api: "resume_upload" } }
      );

      check(res, {
        "resume accepted": (r) =>
          r.status === 200 || r.status === 201,
      });
    });
  }

  sleep(1);
}