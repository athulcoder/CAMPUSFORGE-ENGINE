"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export default function Page() {
  const router = useRouter();
  const [fadeOut, setFadeOut] = useState(false);

  useEffect(() => {
    // Start fade-out after intro animation
    const fadeTimer = setTimeout(() => setFadeOut(true), 2200);

    // Redirect after fade-out completes
    const redirectTimer = setTimeout(() => {
      router.replace("/dashboard");
    }, 3200);

    return () => {
      clearTimeout(fadeTimer);
      clearTimeout(redirectTimer);
    };
  }, [router]);

  return (
    <div
      className={`fixed inset-0 flex items-center justify-center bg-white transition-opacity duration-1000 ease-out ${
        fadeOut ? "opacity-0" : "opacity-100"
      }`}
    >
      <div className="text-center">
        <h1 className="text-4xl md:text-6xl font-semibold tracking-tight text-gray-900 animate-slide-up">
          Campus Forge
          <span className="block text-gray-400 text-base md:text-lg mt-2 font-normal">
            Engine
          </span>
        </h1>

        <div className="mx-auto mt-6 h-[2px] w-24 bg-gray-900 animate-line-grow" />
      </div>

      {/* Animations */}
      <style jsx>{`
        @keyframes slideUp {
          from {
            opacity: 0;
            transform: translateY(28px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        @keyframes lineGrow {
          from {
            width: 0;
          }
          to {
            width: 96px;
          }
        }

        .animate-slide-up {
          animation: slideUp 1.1s ease-out forwards;
        }

        .animate-line-grow {
          animation: lineGrow 0.9s ease-out forwards;
          animation-delay: 0.6s;
        }
      `}</style>
    </div>
  );
}