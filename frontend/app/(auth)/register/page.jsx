"use client";

import { useState } from "react";
import Link from "next/link";
import Image from "next/image";
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
  const [loading, setLoading] = useState(false);

  const handleRegister = async (e) => {
    e.preventDefault();
    if (loading) return;

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
    <div className="relative flex min-h-screen w-full items-center justify-center overflow-hidden p-4 sm:p-6 lg:p-10">
      {/* Alpine Mountain Background Image (Fixed) */}
      <div
        className="absolute inset-0 bg-cover bg-center bg-no-repeat transition-all duration-1000 scale-105"
        style={{ backgroundImage: `url('/images/auth-bg-2.jpg')` }}
      />

      {/* Dark Cyber-Purple Vignette & Blur Overlay */}
      <div className="absolute inset-0 bg-gradient-to-tr from-slate-950/90 via-purple-950/65 to-slate-950/85 backdrop-blur-[3px]" />

      {/* Ambient Neural Glow Blobs */}
      <div className="pointer-events-none absolute -top-32 -left-32 h-[30rem] w-[30rem] rounded-full bg-purple-600/25 blur-[120px]" />
      <div className="pointer-events-none absolute -bottom-32 -right-32 h-[30rem] w-[30rem] rounded-full bg-cyan-500/20 blur-[120px]" />
      <div className="pointer-events-none absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 h-[40rem] w-[40rem] rounded-full bg-violet-600/10 blur-[140px]" />

      {/* Premium Split Glass Card */}
      <div className="ai-glass-card relative z-10 w-full max-w-5xl rounded-3xl overflow-hidden shadow-[0_0_80px_rgba(147,51,234,0.25)] animate-fadeIn grid grid-cols-1 lg:grid-cols-12 border border-purple-500/25">
        
        {/* Left Column: AI Hero Vector & Visual Section (7 cols) */}
        <div className="relative flex flex-col justify-between p-8 sm:p-10 lg:p-12 lg:col-span-7 bg-gradient-to-b from-purple-950/40 to-slate-950/60 border-b lg:border-b-0 lg:border-r border-purple-500/15 overflow-hidden">
          
          {/* Subtle Grid Pattern Overlay */}
          <div className="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px] pointer-events-none" />

          {/* Top Brand Header */}
          <div className="relative z-10">
            <div className="inline-flex items-center gap-2 rounded-full bg-cyan-500/15 px-3.5 py-1.5 text-xs font-semibold text-cyan-300 border border-cyan-400/30 backdrop-blur-md shadow-sm mb-4">
              <span className="relative flex h-2 w-2">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-cyan-400 opacity-75"></span>
                <span className="relative inline-flex rounded-full h-2 w-2 bg-cyan-400"></span>
              </span>
              RECRUITER ONBOARDING
            </div>

            <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-white leading-tight">
              Join Campus Forge <br className="hidden sm:inline" />
              <span className="bg-gradient-to-r from-purple-300 via-pink-300 to-cyan-300 bg-clip-text text-transparent">
                AI Talent Intelligence
              </span>
            </h1>

            <p className="mt-3 text-sm text-slate-300 max-w-lg leading-relaxed">
              Create your account to unlock automated candidate extraction, high-precision resume scoring, and seamless job role matching.
            </p>
          </div>

          {/* Center AI Vector Illustration */}
          <div className="relative z-10 my-8 sm:my-10 flex flex-col items-center justify-center">
            <div className="relative w-full max-w-sm sm:max-w-md aspect-square rounded-2xl overflow-hidden p-2 bg-gradient-to-b from-purple-500/20 via-transparent to-cyan-500/20 border border-purple-500/30 shadow-2xl shadow-purple-950/80 animate-float">
              <Image
                src="/images/ai-illustration.png"
                alt="Campus Forge AI Engine"
                width={500}
                height={500}
                className="w-full h-full object-cover rounded-xl shadow-inner"
                priority
              />
              
              {/* Floating Overlay Badge 1 */}
              <div className="absolute top-4 left-4 z-20 flex items-center gap-2 rounded-xl bg-slate-900/80 backdrop-blur-md px-3 py-2 border border-purple-500/30 text-xs font-medium text-white shadow-xl">
                <div className="flex h-6 w-6 items-center justify-center rounded-lg bg-purple-500/20 text-purple-300">
                  ★
                </div>
                <div>
                  <div className="text-[10px] text-slate-400 uppercase tracking-wider">Talent Pipeline</div>
                  <div className="font-bold text-purple-300">Instant AI Job Match</div>
                </div>
              </div>

              {/* Floating Overlay Badge 2 */}
              <div className="absolute bottom-4 right-4 z-20 flex items-center gap-2 rounded-xl bg-slate-900/80 backdrop-blur-md px-3 py-2 border border-cyan-500/30 text-xs font-medium text-white shadow-xl">
                <span className="h-2 w-2 rounded-full bg-emerald-400 animate-pulse" />
                <span className="text-emerald-300 font-semibold">Ready for Recruiter Setup</span>
              </div>
            </div>
          </div>

          {/* Bottom Feature Badges */}
          <div className="relative z-10 grid grid-cols-3 gap-3 pt-4 border-t border-purple-500/15">
            <div className="flex flex-col items-center text-center">
              <span className="text-base font-bold text-purple-300">Fast Setup</span>
              <span className="text-[11px] text-slate-400">Under 1 Minute</span>
            </div>
            <div className="flex flex-col items-center text-center border-x border-purple-500/15">
              <span className="text-base font-bold text-cyan-300">Smart AI</span>
              <span className="text-[11px] text-slate-400">Automatic Extraction</span>
            </div>
            <div className="flex flex-col items-center text-center">
              <span className="text-base font-bold text-pink-300">Unlimited</span>
              <span className="text-[11px] text-slate-400">Resume Uploads</span>
            </div>
          </div>
        </div>

        {/* Right Column: Premium AI Register Form (5 cols) */}
        <div className="relative flex flex-col justify-center p-8 sm:p-10 lg:p-12 lg:col-span-5 bg-slate-950/80 backdrop-blur-xl">
          
          {/* Logo Badge */}
          <div className="flex flex-col items-center text-center mb-5">
            <div className="mb-3 flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-tr from-purple-600 via-indigo-600 to-cyan-500 shadow-lg shadow-purple-500/30 ring-1 ring-white/20">
              <svg className="h-7 w-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z" />
              </svg>
            </div>
            <h2 className="text-2xl font-bold tracking-tight text-white">
              Create AI Account
            </h2>
            <p className="mt-1 text-xs text-slate-400">
              Fill in your details to start candidate matching
            </p>
          </div>

          {/* Error Alert */}
          {error && (
            <div className="mb-4 flex items-center gap-3 rounded-xl bg-rose-500/15 p-3.5 text-xs text-rose-200 border border-rose-500/30 animate-shake">
              <svg className="h-4 w-4 shrink-0 text-rose-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
              </svg>
              <span>{error}</span>
            </div>
          )}

          {/* Form */}
          <form onSubmit={handleRegister} className="space-y-3.5">
            {/* Full Name */}
            <div>
              <label className="block text-[11px] font-bold uppercase tracking-wider text-slate-300 mb-1">
                Full Name
              </label>
              <div className="relative">
                <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3.5 text-slate-400">
                  <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.8} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                  </svg>
                </div>
                <input
                  type="text"
                  placeholder="John Doe"
                  className="ai-glass-input w-full rounded-xl py-2.5 pr-4 pl-10 text-xs sm:text-sm text-white placeholder-slate-500 outline-none"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                />
              </div>
            </div>

            {/* Email Address */}
            <div>
              <label className="block text-[11px] font-bold uppercase tracking-wider text-slate-300 mb-1">
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
                  placeholder="recruiter@company.com"
                  className="ai-glass-input w-full rounded-xl py-2.5 pr-4 pl-10 text-xs sm:text-sm text-white placeholder-slate-500 outline-none"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>
            </div>

            {/* Password */}
            <div>
              <label className="block text-[11px] font-bold uppercase tracking-wider text-slate-300 mb-1">
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
                  className="ai-glass-input w-full rounded-xl py-2.5 pr-10 pl-10 text-xs sm:text-sm text-white placeholder-slate-500 outline-none"
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

            {/* Checkbox Options */}
            <div className="flex items-center justify-between text-xs text-slate-300 pt-0.5">
              <label className="flex items-center gap-2 cursor-pointer group">
                <input
                  type="checkbox"
                  checked={showPassword}
                  onChange={() => setShowPassword(!showPassword)}
                  className="h-4 w-4 rounded border-slate-700 bg-slate-900 text-purple-500 focus:ring-purple-500/40 focus:ring-offset-0 accent-purple-500 transition cursor-pointer"
                />
                <span className="group-hover:text-white text-xs transition-colors">Show password</span>
              </label>
            </div>

            {/* AI Action Submit Button */}
            <button
              type="submit"
              disabled={loading}
              className={`w-full rounded-xl py-3.5 text-xs sm:text-sm font-semibold text-white shadow-xl transition-all duration-300 cursor-pointer ${
                loading
                  ? "bg-purple-700/60 cursor-not-allowed scale-[0.99]"
                  : "bg-gradient-to-r from-purple-600 via-violet-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 shadow-purple-600/30 hover:shadow-purple-500/50 active:scale-[0.98]"
              }`}
            >
              {loading ? (
                <span className="flex items-center justify-center gap-2">
                  <span className="h-4 w-4 animate-spin rounded-full border-2 border-white border-t-transparent" />
                  Creating account...
                </span>
              ) : (
                <span className="flex items-center justify-center gap-2">
                  <span>Register & Launch Dashboard</span>
                  <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
                  </svg>
                </span>
              )}
            </button>
          </form>

          {/* Footer Navigation Link */}
          <div className="mt-5 text-center border-t border-purple-500/15 pt-4">
            <p className="text-xs text-slate-400">
              Already have an account?{" "}
              <Link
                href="/login"
                className="font-semibold text-purple-400 hover:text-purple-300 hover:underline transition-colors"
              >
                Log in to Dashboard
              </Link>
            </p>
          </div>
        </div>

      </div>
    </div>
  );
}