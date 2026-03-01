"use client";

import { createContext, useContext, useEffect, useState } from "react";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let mounted = true;
    async function fetchUser() {
      try {
        const token = localStorage.getItem('token')

        const res = await fetch(`${process.env.NEXT_PUBLIC_BASE_URL}/api/recruiter/me`, {
          headers:{
            Authorization: `Bearer ${token}`, 

          }
        });

        if (!res.ok) {
          setUser(null);
          return;
        }

        const data = await res.json();

        if (mounted) {
          setUser(data.recruiter); // ✅ FIXED
        }
      } catch (err) {
        console.error("Auth error:", err);
        setUser(null);
      } finally {
        if (mounted) setLoading(false);
      }
    }

    fetchUser();

    return () => {
      mounted = false;
    };
  }, []);

  return (
    <AuthContext.Provider value={{ user, loading }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);