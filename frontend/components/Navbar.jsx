"use client";

import Link from "next/link";
import { useAuth } from "@/context/AuthContext";

function Navbar() {
  const { user, loading } = useAuth();

  return (
    <nav className="sticky top-0 z-50 bg-white border-b">
      <div className="max-w-6xl mx-auto px-6 py-3 flex items-center justify-between">
        {/* Left */}
        <div className="flex items-center gap-8">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-lg bg-blue-600 flex items-center justify-center text-white font-bold">
              C
            </div>
            <span className="font-semibold text-lg">
              Campus Forge Engine
            </span>
          </div>

          <div className="hidden md:flex items-center gap-6 text-sm font-medium text-gray-600">
            <Link href="/dashboard" className="hover:text-blue-600 transition">
              Dashboard
            </Link>
            <Link href="/candidate" className="hover:text-blue-600 transition">
              Candidates
            </Link>
          </div>
        </div>

        {/* Right */}
        <div className="flex items-center gap-4 min-h-[36px]">
          {loading && (
            <>
              <div className="flex flex-col gap-2 items-end">
                <div className="h-3 w-20 rounded bg-gray-200 animate-pulse" />
                <div className="h-4 w-28 rounded bg-gray-200 animate-pulse" />
              </div>
              <div className="w-9 h-9 rounded-full bg-gray-200 animate-pulse" />
            </>
          )}

          {!loading && user && (
            <>
              <div className="text-right leading-tight">
                <p className="text-xs text-gray-500">{user.name}</p>
                <p className="text-sm font-medium">{user.email}</p>
              </div>
              <div className="w-9 h-9 rounded-full bg-gray-200 flex items-center justify-center text-sm font-semibold">
                {user.name?.[0]?.toUpperCase() || "U"}
              </div>
            </>
          )}

          {/* ❌ No login, nothing when user is null */}
        </div>
      </div>
    </nav>
  );
}

export default Navbar;