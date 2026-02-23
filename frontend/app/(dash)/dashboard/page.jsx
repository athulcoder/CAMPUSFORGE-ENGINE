"use client";

import { useState } from "react";
import Link from "next/link";
import {
  Upload,
  FileText,
  Trash2,
  Loader2,
  CheckCircle,
  CircleDot,
  GitBranch,
  Briefcase,
  ArrowRight,
} from "lucide-react";

// Pipeline steps definition
const PIPELINE_STEPS = [
  { key: "queued", label: "Queued", icon: CircleDot },
  { key: "parsing", label: "Parsing Resume", icon: Loader2 },
  { key: "processing", label: "Pipeline Processing", icon: GitBranch },
  { key: "matching", label: "Job Matching", icon: Briefcase },
  { key: "completed", label: "Completed", icon: CheckCircle },
];

export default function RecruiterDashboard() {
  const [files, setFiles] = useState([]);

  const handleUpload = (e) => {
    const uploaded = Array.from(e.target.files).map((file) => ({
      id: crypto.randomUUID(),
      name: file.name,
      size: (file.size / 1024).toFixed(1) + " KB",
      status: "queued",
      stepIndex: 0,
      score: null,
      roles: [],
    }));

    setFiles((prev) => [...uploaded, ...prev]);
    uploaded.forEach((_, idx) => runPipeline(idx));
  };

  const runPipeline = (index) => {
    PIPELINE_STEPS.forEach((step, stepIdx) => {
      setTimeout(() => {
        setFiles((prev) =>
          prev.map((f, i) =>
            i === index
              ? {
                  ...f,
                  status: step.key,
                  stepIndex: stepIdx,
                  ...(step.key === "completed"
                    ? {
                        score: Math.floor(Math.random() * 25) + 75,
                        roles: ["Frontend Engineer", "Full Stack Developer"],
                      }
                    : {}),
                }
              : f
          )
        );
      }, stepIdx * 1500);
    });
  };

  const removeFile = (id) => {
    setFiles((prev) => prev.filter((f) => f.id !== id));
  };

  const StepIcon = ({ step, active }) => {
    const Icon = step.icon;
    return (
      <div
        className={`w-8 h-8 flex items-center justify-center rounded-full border ${
          active
            ? "bg-blue-500 text-white border-blue-500"
            : "bg-gray-100 text-gray-400 border-gray-200"
        }`}
      >
        <Icon
          className={`w-4 h-4 ${
            active && step.key === "parsing" ? "animate-spin" : ""
          }`}
        />
      </div>
    );
  };

  return (
    <div className="min-h-screen bg-gray-50 p-8 text-gray-900">
      <div className="max-w-6xl mx-auto space-y-8">
        <header>
          <h1 className="text-3xl font-semibold">Resume Processing Dashboard</h1>
          <p className="text-gray-500">
            Upload → Queue → Parsing → Processing → Matching
          </p>
        </header>

        {/* Upload */}
        <div className="bg-white border rounded-2xl p-6 shadow-sm">
          <label className="flex flex-col items-center justify-center border-2 border-dashed rounded-xl p-10 cursor-pointer hover:border-blue-500 transition">
            <Upload className="w-10 h-10 text-blue-500 mb-3" />
            <p className="font-medium">Upload resumes (PDF)</p>
            <input
              type="file"
              accept="application/pdf"
              multiple
              className="hidden"
              onChange={handleUpload}
            />
          </label>
        </div>

        {/* Resume Pipeline List */}
        <div className="space-y-4">
          {files.length === 0 ? (
            <p className="text-gray-500">No resumes uploaded yet.</p>
          ) : (
            files.map((file) => (
              <div
                key={file.id}
                className="bg-white border rounded-2xl p-5 shadow-sm"
              >
                {/* Header */}
                <div className="flex items-center justify-between mb-4">
                  <div className="flex items-center gap-3">
                    <FileText className="w-5 h-5 text-blue-500" />
                    <div>
                      <p className="font-medium text-sm">{file.name}</p>
                      <p className="text-xs text-gray-500">{file.size}</p>
                    </div>
                  </div>

                  {/* Remove only if NOT completed */}
                  {file.status !== "completed" && (
                    <button
                      onClick={() => removeFile(file.id)}
                      className="text-red-500 hover:text-red-600"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  )}
                </div>

                {/* Pipeline Steps */}
                <div className="flex items-center justify-between gap-2">
                  {PIPELINE_STEPS.map((step, idx) => (
                    <div key={step.key} className="flex-1 text-center">
                      <StepIcon step={step} active={idx <= file.stepIndex} />
                      <p
                        className={`mt-2 text-xs ${
                          idx <= file.stepIndex
                            ? "text-gray-900 font-medium"
                            : "text-gray-400"
                        }`}
                      >
                        {step.label}
                      </p>
                    </div>
                  ))}
                </div>

                {/* Result + CTA */}
                {file.status === "completed" && (
                  <div className="mt-4 rounded-xl bg-gray-50 p-4 flex items-center justify-between">
                    <div>
                      <p className="text-sm font-medium mb-1">AI Result</p>
                      <p className="text-2xl font-semibold text-green-600">
                        {file.score}% Match
                      </p>
                    </div>

                    <Link
                      href={`/candidate/${file.id}`}
                      className="inline-flex items-center gap-2 text-sm font-medium text-blue-600 hover:text-blue-700"
                    >
                      View Candidate
                      <ArrowRight className="w-4 h-4" />
                    </Link>
                  </div>
                )}
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}
