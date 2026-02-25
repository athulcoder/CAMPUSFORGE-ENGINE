"use client";

import { useState } from "react";
import Link from "next/link";
import {
  Upload,
  FileText,
  Trash2,
  Loader2,
  CircleDot,
  GitBranch,
  Briefcase,
  CheckCircle,
  ArrowRight,
} from "lucide-react";

import { uploadResume } from "./action";

/* ---------------- PIPELINE ---------------- */

const PIPELINE_STEPS = [
  { key: "upload", label: "Upload" },
  { key: "queue", label: "Queued" },
  { key: "parsing", label: "Parsing" },
  { key: "scoring", label: "Scoring" },
  { key: "matching", label: "Matching" },
  { key: "completed", label: "Completed" },
];

/* ---------------- HELPERS ---------------- */

function getStepIndex(status) {
  switch (status) {
    case "PREPARING_UPLOAD":
    case "UPLOADING":
    case "UPLOADED":
      return 0;
    case "QUEUED":
      return 1;
    case "PARSING":
      return 2;
    case "SCORING":
      return 3;
    case "MATCHING":
    case "FINALIZING":
      return 4;
    case "COMPLETED":
      return 5;
    default:
      return 0;
  }
}

function getStatusLabel(status) {
  switch (status) {
    case "PREPARING_UPLOAD":
      return "Preparing upload";
    case "UPLOADING":
      return "Uploading resume";
    case "UPLOADED":
      return "Upload completed";
    case "QUEUED":
      return "Added to queue";
    case "PARSING":
      return "Parsing resume";
    case "SCORING":
      return "Calculating score";
    case "MATCHING":
      return "Matching jobs";
    case "COMPLETED":
      return "Completed";
    case "FAILED":
      return "Failed";
    default:
      return "Pending";
  }
}

/* ---------------- COMPONENT ---------------- */

export default function RecruiterDashboard() {
  const [files, setFiles] = useState([]);

  /* ---------- POLLING ---------- */
  const startPolling = (resumeId) => {
    const interval = setInterval(async () => {
      const res = await fetch(
        `http://localhost:8080/api/resume/${resumeId}/status`,
        { credentials: "include" }
      );

      if (!res.ok) return;

      const data = await res.json();

      setFiles((prev) =>
        prev.map((f) =>
          f.id === resumeId
            ? {
                ...f,
                status: data.status,
                score: data.score ?? f.score,
              }
            : f
        )
      );

      if (["COMPLETED", "FAILED"].includes(data.status)) {
        clearInterval(interval);
      }
    }, 2000);
  };

  /* ---------- UPLOAD ---------- */
  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const tempId = crypto.randomUUID();

    setFiles((prev) => [
      {
        id: tempId,
        name: file.name,
        size: (file.size / 1024).toFixed(1) + " KB",
        status: "PREPARING_UPLOAD",
        progress: 0,
        score: null,
      },
      ...prev,
    ]);

    try {
      setFiles((prev) =>
        prev.map((f) =>
          f.id === tempId ? { ...f, status: "UPLOADING" } : f
        )
      );

      const res = await uploadResume(file, (progress) => {
        setFiles((prev) =>
          prev.map((f) =>
            f.id === tempId ? { ...f, progress } : f
          )
        );
      });

      setFiles((prev) =>
        prev.map((f) =>
          f.id === tempId
            ? {
                ...f,
                id: res.resume_id,
                status: "QUEUED",
                progress: 100,
              }
            : f
        )
      );

      startPolling(res.resume_id);
    } catch (err) {
      console.error(err);
    }
  };

  const removeFile = (id) => {
    setFiles((prev) => prev.filter((f) => f.id !== id));
  };

  /* ---------- RENDER ---------- */
  return (
    <div className="min-h-screen bg-gradient-to-br from-emerald-50 to-white p-8">
      <div className="max-w-6xl mx-auto space-y-10">

        {/* Header */}
        <header>
          <h1 className="text-3xl font-semibold text-gray-900">
            Resume Processing Pipeline
          </h1>
          <p className="text-gray-500 mt-1">
            Async · Redis · Non-blocking
          </p>
        </header>

        {/* Upload */}
        <div className="rounded-2xl border bg-white p-6 shadow-sm">
          <label className="flex flex-col items-center justify-center border-2 border-dashed border-emerald-300 rounded-xl p-10 cursor-pointer hover:bg-emerald-50 transition">
            <Upload className="w-10 h-10 text-emerald-600 mb-2" />
            <p className="font-medium text-gray-700">
              Upload resume (PDF)
            </p>
            <input
              type="file"
              accept="application/pdf"
              className="hidden"
              onChange={handleUpload}
            />
          </label>
        </div>

        {/* List */}
        <div className="space-y-6">
          {files.map((file) => {
            const stepIndex = getStepIndex(file.status);

            return (
              <div
                key={file.id}
                className="rounded-2xl border bg-white/80 backdrop-blur p-6 shadow-sm"
              >
                {/* Top */}
                <div className="flex justify-between items-start">
                  <div className="flex gap-4 items-center">
                    <div className="h-10 w-10 rounded-xl bg-emerald-100 flex items-center justify-center">
                      <FileText className="w-5 h-5 text-emerald-600" />
                    </div>
                    <div>
                      <p className="font-medium text-gray-900">
                        {file.name}
                      </p>
                      <p className="text-xs text-gray-500">
                        {file.size}
                      </p>
                    </div>
                  </div>

                  {file.status !== "COMPLETED" && (
                    <button
                      onClick={() => removeFile(file.id)}
                      className="text-gray-400 hover:text-red-500 transition"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  )}
                </div>

                {/* Status */}
                <div className="mt-4 flex items-center gap-2">
                  {file.status === "UPLOADING" && (
                    <Loader2 className="w-4 h-4 animate-spin text-emerald-600" />
                  )}
                  <span className="text-sm font-medium text-gray-700">
                    {getStatusLabel(file.status)}
                  </span>
                </div>

                {/* Upload Progress */}
                {file.status === "UPLOADING" && (
                  <div className="mt-3">
                    <div className="h-2 bg-gray-200 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-emerald-500 transition-all"
                        style={{ width: `${file.progress}%` }}
                      />
                    </div>
                    <p className="text-xs text-gray-500 mt-1">
                      {file.progress}%
                    </p>
                  </div>
                )}

                {/* Stepper */}
                <div className="mt-6 grid grid-cols-6 gap-2">
                  {PIPELINE_STEPS.map((step, idx) => (
                    <div key={step.key} className="text-center">
                      <div
                        className={`h-2 rounded-full transition ${
                          idx <= stepIndex
                            ? "bg-emerald-500"
                            : "bg-gray-200"
                        }`}
                      />
                      <p className="mt-2 text-xs text-gray-500">
                        {step.label}
                      </p>
                    </div>
                  ))}
                </div>

                {/* Result */}
                {file.status === "COMPLETED" && (
                  <div className="mt-6 flex items-center justify-between rounded-xl bg-emerald-50 p-4">
                    <div>
                      <p className="text-xs text-gray-600">
                        Match Score
                      </p>
                      <p className="text-2xl font-bold text-emerald-600">
                        {file.score}%
                      </p>
                    </div>

                    <Link
                      href={`/candidate/${file.id}`}
                      className="inline-flex items-center gap-2 text-sm font-medium text-emerald-700 hover:text-emerald-800"
                    >
                      View Candidate
                      <ArrowRight className="w-4 h-4" />
                    </Link>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}