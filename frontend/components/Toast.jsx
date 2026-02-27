"use client";

import { useEffect, useState } from "react";

export default function Toast({ message, type = "success", onClose }) {
  const [fadeOut, setFadeOut] = useState(false);

  useEffect(() => {
    const fadeTimer = setTimeout(() => setFadeOut(true), 3000);
    const removeTimer = setTimeout(onClose, 3500);

    return () => {
      clearTimeout(fadeTimer);
      clearTimeout(removeTimer);
    };
  }, [onClose]);

  const colors = {
    success: "bg-green-500",
    error: "bg-red-500",
    warning: "bg-orange-500",
  };

  return (
    <div
      className={`
        fixed top-16 right-6 z-50
        min-w-[260px]
        px-4 py-3
        rounded-lg
        text-white
        shadow-lg
        transition-opacity duration-500
        ${fadeOut ? "opacity-0" : "opacity-100"}
        ${colors[type]}
      `}
    >
      <div className="flex items-center justify-between gap-4">
        <span className="text-sm">{message}</span>
        <button
          onClick={onClose}
          className="text-white/80 hover:text-white text-lg leading-none"
        >
          ×
        </button>
      </div>
    </div>
  );
}