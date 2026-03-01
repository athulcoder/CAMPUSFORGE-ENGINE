"use client";

import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

export default function AuthLayout({ children }) {
  const router = useRouter();
  const [ready, setReady] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("token");

    
    if (token) {
      router.replace("/dashboard");
    } else {
      setReady(true); 
    }
  }, [router]);

  // ⏳ Prevent flicker
  if (!ready) return null;

  return children;
}