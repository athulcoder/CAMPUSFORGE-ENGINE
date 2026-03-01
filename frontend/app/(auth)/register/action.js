export const actionRegister = async (email,name, password) => {
  const res = await fetch(`${process.env.NEXT_PUBLIC_BASE_URL}/api/auth/register`, {
    method: "POST",
    credentials:"include",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password ,name}),
  });

  const data = await res.json();



  return data
};