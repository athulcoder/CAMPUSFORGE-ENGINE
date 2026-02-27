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

/* ---------------- CONFIG ---------------- */

const MAX_FILE_SIZE_MB = 5;

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
  const socketStarted = useRef(false);

  /* ---------- SOCKET (LAZY, ONCE) ---------- */
  const startSocketIfNeeded = () => {
    if (socketStarted.current) return;

    socket.connect();
    socketStarted.current = true;

    socket.on("resume_status", (data) => {
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

  /* ---------- MULTI FILE UPLOAD ---------- */
  const handleUpload = async (e) => {
    const selectedFiles = Array.from(e.target.files || []);
    if (selectedFiles.length === 0) return;

    startSocketIfNeeded();

    for (const file of selectedFiles) {
      // Validate PDF
      if (file.type !== "application/pdf") continue;

      // Validate size
      if (file.size > MAX_FILE_SIZE_MB * 1024 * 1024) {
        alert(`${file.name} exceeds ${MAX_FILE_SIZE_MB}MB`);
        continue;
      }

      await processSingleFile(file);
    }

    e.target.value = ""; // reset input
  };

  /* ---------- SINGLE FILE PIPELINE ---------- */
  const processSingleFile = async (file) => {
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

      // Replace temp ID with resume_id
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

      // Join room for THIS resume
      socket.emit("join_resume", { resume_id: res.resume_id });

    } catch (err) {
      console.error("Upload failed:", err);
      setFiles((prev) =>
        prev.map((f) =>
          f.id === tempId ? { ...f, status: "FAILED" } : f
        )
      );
    }
  };

  const removeFile = (id) => {
    setFiles((prev) => prev.filter((f) => f.id !== id));
  };
  const canRemove = (status) =>
  status === "PREPARING_UPLOAD" || status === "FAILED";

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
            Multi-upload · Redis · WebSockets
          </p>
        </header>

        {/* Upload */}
        <div className="rounded-2xl border bg-white p-6 shadow-sm">
          <label className="flex flex-col items-center justify-center border-2 border-dashed border-emerald-300 rounded-xl p-10 cursor-pointer hover:bg-emerald-50 transition">
            <Upload className="w-10 h-10 text-emerald-600 mb-2" />
            <p className="font-medium text-gray-700">
              Upload resumes (PDF, up to {MAX_FILE_SIZE_MB}MB)
            </p>
            <input
              type="file"
              accept="application/pdf"
              multiple
              className="hidden"
              onChange={handleUpload}
            />
          </label>


        </div>
          <div><a href={'/candidate'} className="bg-yellow-500 text-white rounded-lg px-2 py-3 cursor-pointer">See all candidates</a></div>

        {/* List */}
        <div className="space-y-6">
          {files.map((file) => {
            const stepIndex = getStepIndex(file.status);

            return (
                        <div  
                key={file.id}
                className={`rounded-2xl border p-6 shadow-sm transition ${
                  file.status === "COMPLETED"
                    ? "bg-emerald-50/60"
                    : "bg-white"
                }`}
              >
                {/* Header */}
                <div className="flex justify-between items-start">
                  <div className="flex gap-4 items-center">
                    <div className="h-10 w-10 rounded-xl bg-emerald-100 flex items-center justify-center">
                      <FileText className="w-5 h-5 text-emerald-600" />
                    </div>
                    <div>
                      <p className="font-medium text-gray-900">{file.name}</p>
                      <p className="text-xs text-gray-500">{file.size}</p>
                    </div>
                  </div>

                  {canRemove(file.status) && (
                    <button
                      onClick={() => removeFile(file.id)}
                      className="text-gray-400 hover:text-red-500 transition"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  )}
                </div>

                {/* Status row */}
                <div className="mt-4 flex items-center gap-3">
                  {file.status === "UPLOADING" && (
                    <Loader2 className="w-4 h-4 animate-spin text-emerald-600" />
                  )}

                  <span className="text-sm font-medium text-gray-700">
                    {getStatusLabel(file.status)}
                  </span>

                  {typeof file.progress === "number" && (
                    <span className="ml-auto text-xs font-medium text-gray-500">
                      {file.progress}%
                    </span>
                  )}
                </div>

                {/* Progress bar */}
                {typeof file.progress === "number" && file.status !== "COMPLETED" && (
                  <div className="mt-3 h-2 w-full rounded-full bg-gray-200 overflow-hidden">
                    <div
                      className="h-full rounded-full bg-emerald-500 transition-all duration-300"
                      style={{ width: `${file.progress}%` }}
                    />
                  </div>
                )}

                {file.message && (
                  <p className="text-xs text-green-500 mt-2">{file.message}</p>
                )}

                {/* Pipeline */}
                <div className="mt-6 grid grid-cols-6 gap-2">
                  {PIPELINE_STEPS.map((step, idx) => (
                    <div key={step} className="text-center">
                      <div
                        className={`h-2 rounded-full transition ${
                          idx <= stepIndex ? "bg-emerald-500" : "bg-gray-200"
                        }`}
                      />
                      <p className="mt-2 text-[10px] text-gray-500">{step}</p>
                    </div>
                  ))}
                </div>

                {/* Result */}
                {file.status === "COMPLETED" && (
                  <div className="mt-6 flex items-center justify-between rounded-xl bg-emerald-100/70 p-4">
             

                    <Link
                      href={`/candidate/${file.id}`}
                      className="inline-flex items-center gap-2 text-sm font-medium text-emerald-700 hover:text-emerald-800"
                    >
                      View Candidate
                      <ArrowRight className="w-4 h-4" />
                    </Link>
                  </div>
                )}
              </div>);
          })}
        </div>
      </div>
    </div>
  );
}