"use client";

import { useRef, useState } from "react";
import Link from "next/link";
import { socket } from "@/lib/socket";
import {
  Upload,
  FileText,
  Trash2,
  Loader2,
  ArrowRight,
} from "lucide-react";

import { uploadResume } from "./action";

/* ---------------- PIPELINE ---------------- */

const PIPELINE_STEPS = [
  "UPLOAD",
  "QUEUED",
  "PARSING",
  "SCORING",
  "MATCHING",
  "COMPLETED",
];

function getStepIndex(status) {
  const map = {
    PREPARING_UPLOAD: 0,
    UPLOADING: 0,
    QUEUED: 1,
    PARSING: 2,
    SCORING: 3,
    MATCHING: 4,
    FINALIZING: 4,
    COMPLETED: 5,
  };
  return map[status] ?? 0;
}

function getStatusLabel(status) {
  const map = {
    PREPARING_UPLOAD: "Preparing upload",
    UPLOADING: "Uploading resume",
    QUEUED: "Added to queue",
    PARSING: "Parsing resume",
    SCORING: "Calculating score",
    MATCHING: "Matching jobs",
    COMPLETED: "Completed",
    FAILED: "Failed",
  };
  return map[status] ?? "Pending";
}

/* ---------------- COMPONENT ---------------- */

export default function RecruiterDashboard() {
  const [files, setFiles] = useState([]);

  // 🔑 socket lifecycle guard
  const socketStarted = useRef(false);

  /* ---------- START SOCKET (LAZY) ---------- */
  const startSocketIfNeeded = () => {
    if (socketStarted.current) return;

    socket.connect();
    socketStarted.current = true;

    socket.on("resume_status", (data) => {
      console.log("📩 resume_status", data);

      setFiles((prev) =>
        prev.map((f) =>
          f.id === data.resume_id
            ? {
                ...f,
                status: data.status,
                progress: data.progress ?? f.progress,
                score: data.score ?? f.score,
                message: data.message ?? f.message,
              }
            : f
        )
      );
    });
  };

  /* ---------- UPLOAD ---------- */
  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    // 🔑 Start socket ONLY now
    startSocketIfNeeded();

    const tempId = crypto.randomUUID();

    setFiles((prev) => [
      {
        id: tempId,
        name: file.name,
        size: (file.size / 1024).toFixed(1) + " KB",
        status: "PREPARING_UPLOAD",
        progress: 0,
        score: null,
        message: null,
      },
      ...prev,
    ]);

    try {
      // uploading
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

      // replace temp ID with backend resume_id
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

      // 🔑 Join room AFTER resume_id exists
      socket.emit("join_resume", { resume_id: res.resume_id });

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
            Async · Redis · WebSockets
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
                className="rounded-2xl border bg-white p-6 shadow-sm"
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

                {file.message && (
                  <p className="text-xs text-gray-500 mt-1">
                    {file.message}
                  </p>
                )}

                {/* Stepper */}
                <div className="mt-6 grid grid-cols-6 gap-2">
                  {PIPELINE_STEPS.map((step, idx) => (
                    <div key={step} className="text-center">
                      <div
                        className={`h-2 rounded-full ${
                          idx <= stepIndex
                            ? "bg-emerald-500"
                            : "bg-gray-200"
                        }`}
                      />
                      <p className="mt-2 text-xs text-gray-500">
                        {step}
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