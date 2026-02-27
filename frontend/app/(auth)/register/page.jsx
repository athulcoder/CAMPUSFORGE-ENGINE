"use client";

import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { actionRegister } from "./action";
import { useToast } from "@/components/ToastProvider";

export default function RegisterPage() {
  const router = useRouter();
  const { showToast } = useToast();

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false); // UI-only

  const handleRegister = async (e) => {
    e.preventDefault();
    if (loading) return; // 🔒 one click only

    if (!name || !email || !password) {
      setError("All fields are required");
      return;
    }

    setError("");
    setLoading(true);

    const data = await actionRegister(email, name, password);

    if (!data.success) {
      setError(data.error || "Something went wrong");
      setLoading(false);
      return;
    }

    showToast(data.message || "Account created, please login");
    router.replace("/login");
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-gradient-to-br from-gray-50 to-gray-100">
      <div className="w-full max-w-md rounded-2xl bg-white p-8 shadow-lg animate-fadeIn">
        <h1 className="mb-1 text-center text-2xl font-semibold tracking-tight">
          Campus Forge Engine
        </h1>
        <p className="mb-6 text-center text-sm text-gray-500">
          Create your account
        </p>

        {error && (
          <div className="mb-4 rounded-lg bg-red-50 px-3 py-2 text-sm text-red-600 animate-shake">
            {error}
          </div>
        )}

        <form onSubmit={handleRegister} className="space-y-4">
          {/* Name */}
          <div>
            <label className="block text-sm font-medium mb-1">Name</label>
            <input
              type="text"
              placeholder="John Doe"
              className="w-full rounded-lg border px-3 py-2 text-sm transition
                         focus:border-blue-500 focus:ring-2 focus:ring-blue-100
                         outline-none"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>

          {/* Email */}
          <div>
            <label className="block text-sm font-medium mb-1">Email</label>
            <input
              type="email"
              placeholder="you@company.com"
              className="w-full rounded-lg border px-3 py-2 text-sm transition
                         focus:border-blue-500 focus:ring-2 focus:ring-blue-100
                         outline-none"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>

          {/* Password */}
          <div>
            <label className="block text-sm font-medium mb-1">Password</label>
            <input
              type={showPassword ? "text" : "password"}
              placeholder="••••••••"
              className="w-full rounded-lg border px-3 py-2 text-sm transition
                         focus:border-green-500 focus:ring-2 focus:ring-green-100
                         outline-none"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>

          {/* Options */}
          <label className="flex items-center gap-2 text-sm cursor-pointer">
            <input
              type="checkbox"
              className="accent-green-500"
              onChange={() => setShowPassword(!showPassword)}
            />
            Show password
          </label>

          {/* Register Button */}
          <button
            type="submit"
            disabled={loading}
            className={`w-full rounded-lg py-3 text-sm font-medium text-white
              transition-all duration-300
              ${
                loading
                  ? "bg-green-400 cursor-not-allowed scale-[0.99]"
                  : "bg-green-600 hover:bg-green-700 active:scale-[0.98]"
              }`}
          >
            {loading ? (
              <span className="flex items-center justify-center gap-2">
                <span className="h-4 w-4 animate-spin rounded-full border-2 border-white border-t-transparent" />
                Creating account…
              </span>
            ) : (
              "Register"
            )}
          </button>
        </form>

        <p className="mt-6 text-center text-sm text-gray-500">
          Already have an account?{" "}
          <Link href="/login" className="text-blue-500 hover:underline">
            Login
          </Link>
        </p>
      </div>
    </div>
  );
}