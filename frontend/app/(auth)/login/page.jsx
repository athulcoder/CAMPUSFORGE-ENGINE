"use client";

import Link from "next/link";
import Image from "next/image";
import { actionLogin } from "./actions";
import { useToast } from "@/components/ToastProvider";
import { useRouter } from "next/navigation";
import { useState } from "react";

export default function LoginPage() {
  const router = useRouter();
  const { showToast } = useToast();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();
    if (loading) return;

    if (!email || !password) {
      setError("Email and password are required");
      return;
    }

    setError("");
    setLoading(true);

    const data = await actionLogin(email, password);

    if (!data.success) {
      setError(data.error || "Something went wrong");
      setLoading(false);
      return;
    }

    showToast(data.message);
    router.replace("/dashboard");
  };

  return (
    <div className="relative flex min-h-screen lg:h-screen w-full lg:w-screen items-center justify-center p-4 sm:p-6 lg:p-8 overflow-y-auto lg:overflow-hidden">
      {/* Alpine Background */}
      <div
        className="fixed inset-0 bg-cover bg-center bg-no-repeat transition-all duration-700 scale-105"
        style={{ backgroundImage: `url('/images/auth-bg-2.jpg')` }}
      />

      {/* Dynamic Gradient Overlay with Ambient Glow */}
      <div className="fixed inset-0 bg-gradient-to-t from-slate-950/90 via-purple-950/40 to-slate-950/80 backdrop-blur-[3px]" />

      {/* Ambient Glow Orbs */}
      <div className="pointer-events-none fixed top-10 left-1/2 -translate-x-1/2 lg:top-12 lg:left-20 h-64 w-64 lg:h-96 lg:w-96 rounded-full bg-purple-600/30 blur-[100px]" />
      <div className="pointer-events-none fixed bottom-10 right-10 h-64 w-64 lg:h-96 lg:w-96 rounded-full bg-cyan-500/20 blur-[100px]" />

      {/* Main Glass Card Container */}
      <div className="apple-glass-card relative z-10 w-full max-w-md lg:max-w-4xl max-h-none lg:max-h-[620px] rounded-3xl overflow-hidden animate-fadeIn grid grid-cols-1 lg:grid-cols-12 border border-white/20 shadow-[0_25px_60px_-15px_rgba(0,0,0,0.7)]">

        {/* Left Hero Panel (Desktop only: 7 cols) */}
        <div className="hidden lg:flex lg:col-span-7 flex-col justify-between p-8 xl:p-10 bg-slate-950/40 border-r border-white/10 overflow-hidden">
          <div>
            <div className="inline-flex items-center gap-2 rounded-full bg-white/10 px-3.5 py-1 text-xs font-medium text-slate-200 border border-white/15 backdrop-blur-md mb-4">
              <span>Campus Forge Engine</span>
              <span className="text-slate-500">•</span>
              <span className="text-purple-300">Recruiter Portal</span>
            </div>

            <h1 className="text-3xl xl:text-4xl font-semibold tracking-tight text-white leading-tight">
              Talent Intelligence. <br />
              <span className="bg-gradient-to-r from-purple-200 via-pink-200 to-cyan-200 bg-clip-text text-transparent font-normal">
                Reimagined.
              </span>
            </h1>

            <p className="mt-2.5 text-xs text-slate-300 max-w-sm leading-relaxed">
              Seamlessly evaluate candidate profiles, calculate resume match metrics, and accelerate recruitment.
            </p>
          </div>

          {/* Product Graphic Display */}
          <div className="my-4 flex justify-center">
            <div className="relative w-full max-w-xs rounded-2xl overflow-hidden border border-white/20 shadow-2xl bg-slate-900/60 p-2">
              <Image
                src="/images/ai-illustration.png"
                alt="Campus Forge Engine"
                width={400}
                height={400}
                className="w-full h-auto max-h-44 object-cover rounded-xl"
                priority
              />
            </div>
          </div>

          {/* Stat Strip */}
          <div className="grid grid-cols-3 gap-2 pt-4 border-t border-white/10 text-[11px] text-slate-400">
            <div>
              <div className="font-semibold text-white">Instant</div>
              <div>Profile Parsing</div>
            </div>
            <div className="border-x border-white/10 px-1 text-center">
              <div className="font-semibold text-white">Automated</div>
              <div>Match Analytics</div>
            </div>
            <div className="text-right">
              <div className="font-semibold text-white">Enterprise</div>
              <div>Security</div>
            </div>
          </div>
        </div>

        {/* Right Form Panel (Full width on mobile, 5 cols on desktop) */}
        <div className="col-span-1 lg:col-span-5 flex flex-col justify-center p-6 sm:p-8 xl:p-9 bg-slate-950/75 backdrop-blur-2xl">

          {/* Mobile & Header Title Section */}
          <div className="flex flex-col items-center text-center lg:items-start lg:text-left mb-6">

            {/* Mobile Graphic Badge (Visible on mobile/tablet) */}
            <div className="lg:hidden mb-4 relative">
              <div className="w-20 h-20 sm:w-24 sm:h-24 rounded-2xl border border-white/25 shadow-2xl bg-slate-900/80 p-1.5 overflow-hidden">
                <Image
                  src="/images/ai-illustration.png"
                  alt="Campus Forge Engine"
                  width={200}
                  height={200}
                  className="w-full h-full object-cover rounded-xl"
                />
              </div>
              <div className="absolute -bottom-2 -right-2 bg-purple-600 text-white p-1.5 rounded-xl shadow-lg border border-white/20">
                <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </div>
            </div>

            <div className="inline-flex items-center gap-1.5 rounded-full bg-purple-500/15 px-3 py-1 text-[11px] font-medium text-purple-300 border border-purple-500/30 mb-2">
              Recruiter Portal
            </div>

            <h2 className="text-2xl sm:text-3xl font-semibold tracking-tight text-white">
              Sign In
            </h2>
            <p className="mt-1 text-xs text-slate-300">
              Enter your credentials to manage candidate evaluation
            </p>
          </div>

          {/* Error Alert */}
          {error && (
            <div className="mb-4 flex items-center gap-2.5 rounded-xl bg-red-500/15 p-3 text-xs text-red-200 border border-red-500/30 animate-shake">
              <svg className="h-4 w-4 shrink-0 text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
              </svg>
              <span>{error}</span>
            </div>
          )}

          {/* Form */}
          <form onSubmit={handleLogin} className="space-y-4">
            {/* Work Email */}
            <div>
              <label className="block text-xs font-medium text-slate-300 mb-1.5">
                Work Email
              </label>
              <div className="relative">
                <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3.5 text-slate-400">
                  <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.8} d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207" />
                  </svg>
                </div>
                <input
                  type="email"
                  placeholder="name@company.com"
                  className="apple-glass-input w-full rounded-xl py-3 pr-4 pl-10 text-xs sm:text-sm text-white placeholder-slate-500 outline-none"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>
            </div>

            {/* Password */}
            <div>
              <label className="block text-xs font-medium text-slate-300 mb-1.5">
                Password
              </label>
              <div className="relative">
                <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3.5 text-slate-400">
                  <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.8} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                  </svg>
                </div>
                <input
                  type={showPassword ? "text" : "password"}
                  placeholder="••••••••"
                  className="apple-glass-input w-full rounded-xl py-3 pr-10 pl-10 text-xs sm:text-sm text-white placeholder-slate-500 outline-none"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute inset-y-0 right-0 flex items-center pr-3.5 text-slate-400 hover:text-slate-200 transition-colors cursor-pointer"
                  title={showPassword ? "Hide password" : "Show password"}
                >
                  {showPassword ? (
                    <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.8} d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858-5.908a10.025 10.025 0 014.122-.863c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411" />
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.8} d="M3 3l18 18" />
                    </svg>
                  ) : (
                    <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.8} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.8} d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                    </svg>
                  )}
                </button>
              </div>
            </div>



            {/* Premium Button */}
            <button
              type="submit"
              disabled={loading}
              className={`w-full rounded-xl py-3.5 text-xs sm:text-sm font-semibold text-slate-950 bg-gradient-to-r from-slate-100 via-white to-slate-100 hover:from-white hover:to-white shadow-xl hover:shadow-white/20 active:scale-[0.98] transition-all duration-200 cursor-pointer ${loading ? "opacity-75 cursor-not-allowed" : ""
                }`}
            >
              {loading ? (
                <span className="flex items-center justify-center gap-2">
                  <span className="h-4 w-4 animate-spin rounded-full border-2 border-slate-950 border-t-transparent" />
                  Signing in...
                </span>
              ) : (
                "Sign In"
              )}
            </button>
          </form>

          {/* Footer Navigation Link */}
          <div className="mt-6 text-center border-t border-white/10 pt-4">
            <p className="text-xs text-slate-400">
              Don’t have an account?{" "}
              <Link
                href="/register"
                className="font-semibold text-purple-300 hover:text-purple-200 hover:underline transition-colors"
              >
                Create Account
              </Link>
            </p>
          </div>
        </div>

      </div>
    </div>
  );
}