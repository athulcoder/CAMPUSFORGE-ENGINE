import http from "k6/http";
import { check, sleep, fail } from "k6";
import { Trend } from "k6/metrics";

/* ================= METRICS ================= */
const loginLatency = new Trend("login_latency");
const getOneLatency = new Trend("get_one_latency");

/* ================= OPTIONS ================= */
export const options = {
  vus: 1,
  iterations: 1,
  summaryTrendStats: ["avg", "min", "med", "max", "p(90)", "p(95)"],
};

/* ================= CONFIG ================= */
const BASE_URL = "http://localhost:8080";

/* EXISTING USER (must exist) */
const USER = {
  email: "test@email.com",
  password: "123456",
};

/* EXISTING RESUME ID */
const RESUME_ID = "e5feac97-2841-4ae0-881a-c80953666940";

/* ================= TEST ================= */
export default function () {
  /* ---------- LOGIN ---------- */
  const loginRes = http.post(
    `${BASE_URL}/api/auth/login`,
    JSON.stringify(USER),
    { headers: { "Content-Type": "application/json" } }
  );

  loginLatency.add(loginRes.timings.duration);

  check(loginRes, {
    "login success": (r) => r.status === 200,
  });

  const accessToken = loginRes.json("access_token");
  if (!accessToken) {
    fail("❌ access_token not returned from login");
  }

  const authHeaders = {
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  };

  sleep(1);

  /* ---------- GET SINGLE CANDIDATE ---------- */
  const oneRes = http.get(
    `${BASE_URL}/api/candidate/${RESUME_ID}`,
    authHeaders
  );

  getOneLatency.add(oneRes.timings.duration);

  check(oneRes, {
    "get single candidate": (r) => r.status === 200,
  });

  sleep(1);
}