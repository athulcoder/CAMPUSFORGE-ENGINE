export const actionLogin = async (email, password) => {
  const res = await fetch("http://localhost:8080/api/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });

  const data = await res.json();

  // Handle HTTP-level errors
  if (!res.ok) {
    return {
      success: false,
      error: data.error || "Login failed",
      status: res.status,
    };
  }

  return {
    success: true,
    data,
  };
};