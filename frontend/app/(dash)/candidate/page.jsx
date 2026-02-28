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
const STATUS_FILTER = ["PENDING", "ACCEPTED", "REJECTED"];
/* ---------------- COMPONENT ---------------- */

export default function CandidatesPage() {
  const [candidates, setCandidates] = useState([]);
  const [selectedRole, setSelectedRole] = useState("All");
  const [open, setOpen] = useState(false);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(false);


  const [actionState, setActionState] = useState(null);


  const [actionLoading, setActionLoading] = useState(false);

  const [selectedStatus, setSelectedStatus] = useState("PENDING");
  const [statusOpen, setStatusOpen] = useState(false);
  /* ---------- FETCH CANDIDATES ---------- */
  useEffect(() => {
   const fetchCandidates = async () => {
      setLoading(true);
      try {
        const params = new URLSearchParams();

        if (selectedRole !== "All") {
          params.append("role", selectedRole);
        }

        params.append("status", selectedStatus);

        const res = await fetch(
          `http://localhost:8080/api/candidate?${params.toString()}`,
          { credentials: "include" }
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
  }, [selectedRole,selectedStatus]);

  const filteredRoles = JOB_ROLE.filter((role) =>
    role.toLowerCase().includes(search.toLowerCase())
  );



const submitReview = async () => {
  if (!actionState?.note?.trim()) return;

  setActionLoading(true);

  try {
    await fetch(
      `http://localhost:8080/api/resume/${actionState.id}/${actionState.type === "accept" ? "approve" : "reject"}`,
      {
        method: "POST",
        credentials: "include", // IMPORTANT (session cookie)
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          review_note: actionState.note,
        }),
      }
    );

    if (selectedStatus === "PENDING") {
    setCandidates((prev) =>
    prev.filter((c) => c.id !== actionState.id)
    );
}

    setActionState(null);
  } catch (err) {
    console.error(err);
  } finally {
    setActionLoading(false);
  }
};








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
              Resumes ranked by match score
            </p>
          </div>


          {/* Status Filter */}
          <div className="relative w-full md:w-52">
            <button
              onClick={() => setStatusOpen(!statusOpen)}
              className="w-full flex items-center justify-between px-4 py-2 bg-white border rounded-lg text-sm text-gray-700 hover:border-gray-400 transition"
            >
              <span>{selectedStatus}</span>
              <ChevronDown className="w-4 h-4 text-gray-400" />
            </button>

            {statusOpen && (
              <div className="absolute z-20 mt-2 w-full bg-white border rounded-xl shadow-lg">
                {STATUS_FILTER.map((status) => (
                  <div
                    key={status}
                    onClick={() => {
                      setSelectedStatus(status);
                      setStatusOpen(false);
                    }}
                    className={`px-4 py-2 text-sm cursor-pointer hover:bg-emerald-50 ${
                      selectedStatus === status
                        ? "bg-emerald-100 text-emerald-700 font-medium"
                        : "text-gray-700"
                    }`}
                  >
                    {status}
                  </div>
                ))}
              </div>
            )}
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
                       Matching role:  {candidate.job_role}
                      </div>
                    </div>
                  </div>

                  {/* Score */}
                  <div className="min-w-45">
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
                 {candidate.status==="PENDING"?(
                   <div className="flex flex-col items-end gap-2">
                    <div className="flex items-center gap-3">
                      <button
                        onClick={() =>
                          setActionState({
                            id: candidate.id,
                            type: "accept",
                            note: "",
                          })
                        }
                        className="inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium bg-emerald-600 text-white hover:bg-emerald-700"
                      >
                        <Check className="w-4 h-4" />
                        Accept
                      </button>

                      <button
                        onClick={() =>
                          setActionState({
                            id: candidate.id,
                            type: "reject",
                            note: "",
                          })
                        }
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

                    {/* Review input (only for active candidate) */}
                    {actionState?.id === candidate.id && (
                      <div className="w-full mt-2 flex gap-2">
                        <input
                          type="text"
                          placeholder="Add review note..."
                          value={actionState.note}
                          onChange={(e) =>
                            setActionState({
                              ...actionState,
                              note: e.target.value,
                            })
                          }
                          className="flex-1 px-3 py-2 text-sm border rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500"
                        />

                        <button
                          onClick={submitReview}
                          disabled={actionLoading}
                          className={`px-4 py-2 rounded-lg text-sm font-medium text-white ${
                            actionState.type === "accept"
                              ? "bg-emerald-600 hover:bg-emerald-700"
                              : "bg-red-600 hover:bg-red-700"
                          }`}
                        >
                          {actionLoading ? (
                            <Loader2 className="w-4 h-4 animate-spin" />
                          ) : actionState.type === "accept" ? (
                            "Confirm"
                          ) : (
                            "Confirm"
                          )}
                        </button>
                      </div>
                    )}
                  </div>
                 ):""}
                  
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}