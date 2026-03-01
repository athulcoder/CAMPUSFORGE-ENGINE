"use client";

import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

export default function AuthLayout({ children }) {
  const router = useRouter();
  const [ready, setReady] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("token");

    // 🔄 If already logged in → go to dashboard
    if (token) {
      router.replace("/dashboard");
    } else {
      setReady(true); // allow login/register
    }
  }, [router]);

  // ⏳ Prevent flicker
  if (!ready) return null;

  return children;
}