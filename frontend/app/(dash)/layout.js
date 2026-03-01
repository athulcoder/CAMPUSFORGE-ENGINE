"use client";

import Navbar from "@/components/Navbar";
import { AuthProvider } from "@/context/AuthContext";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

export default function ProtectedLayout({ children }) {
  const router = useRouter();
  const [ready, setReady] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("token");

    if (!token) {
      router.replace("/login");
    } else {
      setReady(true); 
    }
  }, [router]);

  if (!ready) return null; 

  return (
    <AuthProvider>
      <Navbar />
      {children}
    </AuthProvider>
  );
}