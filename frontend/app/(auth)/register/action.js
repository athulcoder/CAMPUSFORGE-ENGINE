export const actionRegister = async (email,name, password) => {
  const res = await fetch("http://localhost:8080/api/auth/register", {
    method: "POST",
    credentials:"include",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password ,name}),
  });

  const data = await res.json();



  return data
};