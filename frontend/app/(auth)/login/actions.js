export const actionLogin = async (email, password) => {
  const res = await fetch("http://localhost:8080/api/auth/login", {
    method: "POST",
    credentials:"include",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });

  const data = await res.json();

  // console.log(data)

  return data
};