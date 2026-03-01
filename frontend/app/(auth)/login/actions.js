export const actionLogin = async (email, password) => {
  const res = await fetch(
    `${process.env.NEXT_PUBLIC_BASE_URL}/api/auth/login`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    }
  );

  // Always check response
  if (!res.ok) {
    throw new Error("Login failed");
  }

  const data = await res.json();

  /*
    Backend returns:
    {
      success: true,
      access_token: "...",
      recruiter: {...}
    }
  */

  // 🔐 Store JWT (simple & common)
  if (data.access_token) {
    localStorage.setItem("token", data.access_token);
  }

  return data;
};