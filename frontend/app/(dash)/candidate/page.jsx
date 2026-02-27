"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import {
  User,
  ArrowRight,
  Briefcase,
  BarChart3,
  Hash,
  Check,
  X,
  ChevronDown,
  Loader2,
} from "lucide-react";

/* ---------------- ROLES ---------------- */

const JOB_ROLE = [
  "All",
  "Frontend Engineer",
  "Backend Engineer",
  "Full Stack Developer",
  "React Developer",
  "Node.js Developer",
  "Next.js Developer",
  "Mobile App Developer",
  "Flutter Developer",
  "React Native Developer",
  "UI/UX Designer",
  "Product Engineer",
  "Software Engineer",
  "DevOps Engineer",
  "Cloud Engineer",
  "AI Engineer",
  "ML Engineer",
  "Data Scientist",
  "Data Analyst",
  "System Engineer",
  "Security Engineer",
  "QA Engineer",
  "Automation Engineer",
  "Blockchain Developer",
  "Game Developer",
  "AR/VR Developer",
  "Embedded Engineer",
  "IoT Engineer",
  "Site Reliability Engineer",
  "Tech Lead",
  "Engineering Manager",
];

/* ---------------- COMPONENT ---------------- */

export default function CandidatesPage() {
  const [candidates, setCandidates] = useState([]);
  const [selectedRole, setSelectedRole] = useState("All");
  const [open, setOpen] = useState(false);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(false);

  /* ---------- FETCH CANDIDATES ---------- */
  useEffect(() => {
    const fetchCandidates = async () => {
      setLoading(true);
      try {
        const res = await fetch(
          `http://localhost:8080/api/candidate?role=${encodeURIComponent(selectedRole)}`
        );
        const data = await res.json();
        setCandidates(data.candidates || []);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchCandidates();
  }, [selectedRole]);

  const filteredRoles = JOB_ROLE.filter((role) =>
    role.toLowerCase().includes(search.toLowerCase())
  );

  /* ---------------- UI ---------------- */

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <div className="max-w-5xl mx-auto space-y-8">

        {/* Header */}
        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
          <div>
            <h1 className="text-3xl font-semibold text-gray-900">
              Candidates
            </h1>
            <p className="text-gray-500 mt-1">
              AI-evaluated resumes ranked by match score
            </p>
          </div>

          {/* Role Filter */}
          <div className="relative w-full md:w-72">
            <button
              onClick={() => setOpen(!open)}
              className="w-full flex items-center justify-between px-4 py-2 bg-white border rounded-lg text-sm text-gray-700 hover:border-gray-400 transition"
            >
              <span>{selectedRole}</span>
              <ChevronDown className="w-4 h-4 text-gray-400" />
            </button>

            {open && (
              <div className="absolute z-20 mt-2 w-full bg-white border rounded-xl shadow-lg">
                <input
                  type="text"
                  placeholder="Search roles..."
                  value={search}
                  onChange={(e) => setSearch(e.target.value)}
                  className="w-full px-3 py-2 text-sm border-b outline-none"
                />

                <div className="max-h-64 overflow-y-auto">
                  {filteredRoles.map((role) => (
                    <div
                      key={role}
                      onClick={() => {
                        setSelectedRole(role);
                        setOpen(false);
                        setSearch("");
                      }}
                      className={`px-4 py-2 text-sm cursor-pointer hover:bg-emerald-50 ${
                        selectedRole === role
                          ? "bg-emerald-100 text-emerald-700 font-medium"
                          : "text-gray-700"
                      }`}
                    >
                      {role}
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Content */}
        {loading ? (
          <div className="flex justify-center py-20">
            <Loader2 className="w-6 h-6 animate-spin text-emerald-600" />
          </div>
        ) : candidates.length === 0 ? (
          <p className="text-gray-500 text-center py-20">
            No candidates found for this role.
          </p>
        ) : (
          <div className="space-y-4">
            {candidates.map((candidate) => (
              <div
                key={candidate.id}
                className="bg-white border rounded-2xl p-6 shadow-sm hover:shadow-md transition"
              >
                <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-6">

                  {/* Info */}
                  <div className="flex items-center gap-4">
                    <div className="w-12 h-12 rounded-full bg-emerald-100 flex items-center justify-center">
                      <User className="w-6 h-6 text-emerald-600" />
                    </div>

                    <div>
                      <p className="font-medium text-gray-900">
                        {candidate.name}
                      </p>
                      <p className="text-xs text-gray-500 flex items-center gap-1">
                        <Hash className="w-3 h-3" />
                        {candidate.id}
                      </p>
                      <div className="mt-1 flex items-center gap-2 text-sm text-gray-600">
                        <Briefcase className="w-4 h-4" />
                        {candidate.job_role}
                      </div>
                    </div>
                  </div>

                  {/* Score */}
                  <div className="min-w-[180px]">
                    <div className="flex items-center gap-2 text-sm text-gray-600 mb-1">
                      <BarChart3 className="w-4 h-4" />
                      Match Score
                    </div>

                    <div className="w-full bg-gray-200 rounded-full h-2 overflow-hidden">
                      <div
                        className="bg-emerald-500 h-2 rounded-full transition-all"
                        style={{ width: `${candidate.score}%` }}
                      />
                    </div>

                    <p className="text-right text-sm font-medium text-emerald-600 mt-1">
                      {candidate.score}%
                    </p>
                  </div>

                  {/* Actions */}
                  <div className="flex items-center gap-3">
                    <button
                      className="inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium bg-emerald-600 text-white hover:bg-emerald-700"
                    >
                      <Check className="w-4 h-4" />
                      Accept
                    </button>

                    <button
                      className="inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium bg-red-100 text-red-600 hover:bg-red-200"
                    >
                      <X className="w-4 h-4" />
                      Reject
                    </button>

                    <Link
                      href={`/candidate/${candidate.id}`}
                      className="inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium text-emerald-600 hover:bg-emerald-50"
                    >
                      View
                      <ArrowRight className="w-4 h-4" />
                    </Link>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}