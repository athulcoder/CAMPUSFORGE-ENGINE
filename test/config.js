export const BASE_URL = "http://localhost:8080";

export const USER = {
  email: "mail@email.com",
  password: "123456",
};

export const OPTIONS_UNIT = {
  vus: 1,
  iterations: 1,
};

export const OPTIONS_LOAD = {
  stages: [
    { duration: "20s", target: 5 },
    { duration: "30s", target: 10 },
    { duration: "30s", target: 20 },
    { duration: "20s", target: 0 },
  ],
  thresholds: {
    http_req_failed: ["rate<0.01"],
    http_req_duration: ["p95<800"],
  },
};