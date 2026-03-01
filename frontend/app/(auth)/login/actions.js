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


  const data = await res.json();

  

  if (data.access_token) {
    localStorage.setItem("token", data.access_token);
  }

  return data;
};