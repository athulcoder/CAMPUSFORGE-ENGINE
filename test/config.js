// config.js

export const BASE_URL = "http://localhost:8080";

export const USERS_20 = {
  vus: 20,          // 👈 20 concurrent users
  duration: "2m",   // test runs for 2 minutes
};

export const OPTIONS_20_USERS = {
  vus: 20,
  duration: "2m",

  thresholds: {
    http_req_failed: ["rate<0.01"],

    // AUTH
    "http_req_duration{api:register}": ["p(95)<800"],
    "http_req_duration{api:login}": ["p(95)<700"],

    // REDIS (FAST READS)
    "http_req_duration{api:candidate_all}": ["p(95)<250"],
    "http_req_duration{api:candidate_role}": ["p(95)<250"],

    // DB / MIXED
    "http_req_duration{api:candidate_id}": ["p(95)<350"],

    // ASYNC UPLOAD
    "http_req_duration{api:resume_upload}": ["p(95)<4000"],
  },
};