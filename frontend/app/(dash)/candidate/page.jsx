"use client";

import { useState } from "react";
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
} from "lucide-react";

// Job roles (30+ scalable)
const JOB_ROLES = [
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

// Dummy data
const candidates = [
  { id: "cf-1021", name: "Arjun Menon", role: "Frontend Engineer", score: 92 },
  { id: "cf-1022", name: "Sneha Nair", role: "Full Stack Developer", score: 88 },
  { id: "cf-1023", name: "Rahul Das", role: "Backend Engineer", score: 81 },
];

export default function CandidatesPage() {
  const [selectedRole, setSelectedRole] = useState("All");
  const [open, setOpen] = useState(false);
  const [search, setSearch] = useState("");

  const filteredRoles = JOB_ROLES.filter((role) =>
    role.toLowerCase().includes(search.toLowerCase())
  );

  const filteredCandidates =
    selectedRole === "All"
      ? candidates
      : candidates.filter((c) => c.role === selectedRole);

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <div className="max-w-5xl mx-auto space-y-6">
        {/* Header */}
        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
          <div>
            <h1 className="text-3xl font-semibold text-gray-900">
              All Candidates
            </h1>
            <p className="text-gray-500 mt-1">
              AI-evaluated candidates from Campus Forge Engine
            </p>
          </div>

          {/* Role Filter Combobox */}
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
                      className={`px-4 py-2 text-sm cursor-pointer hover:bg-blue-50 ${
                        selectedRole === role
                          ? "bg-blue-100 text-blue-700 font-medium"
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

        {/* Candidate List */}
        <div className="space-y-4">
          {filteredCandidates.length === 0 ? (
            <p className="text-gray-500">No candidates found.</p>
          ) : (
            filteredCandidates.map((candidate) => (
              <div
                key={candidate.id}
                className="bg-white border rounded-2xl p-6 shadow-sm hover:shadow-md transition"
              >
                <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-6">
                  {/* Info */}
                  <div className="flex items-center gap-4">
                    <div className="w-12 h-12 rounded-full bg-blue-100 flex items-center justify-center">
                      <User className="w-6 h-6 text-blue-600" />
                    </div>
                    <div>
                      <p className="font-medium text-gray-900">
                        {candidate.name}
                      </p>
                      <p className="text-xs text-gray-500 flex items-center gap-1">
                        <Hash className="w-3 h-3" /> {candidate.id}
                      </p>
                      <div className="mt-1 flex items-center gap-2 text-sm text-gray-600">
                        <Briefcase className="w-4 h-4" />
                        {candidate.role}
                      </div>
                    </div>
                  </div>

                  {/* Score */}
                  <div className="min-w-[180px]">
                    <div className="flex items-center gap-2 text-sm text-gray-600 mb-1">
                      <BarChart3 className="w-4 h-4" />
                      Resume Score
                    </div>
                    <div className="w-full bg-gray-200 rounded-full h-2">
                      <div
                        className="bg-green-500 h-2 rounded-full"
                        style={{ width: `${candidate.score}%` }}
                      />
                    </div>
                    <p className="text-right text-sm font-medium text-green-600 mt-1">
                      {candidate.score}%
                    </p>
                  </div>

                  {/* Actions */}
                  <div className="flex items-center gap-3">
                    <button className="inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium bg-green-600 text-white hover:bg-green-700">
                      <Check className="w-4 h-4" />
                      Accept
                    </button>

                    <button className="inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium bg-red-100 text-red-600 hover:bg-red-200">
                      <X className="w-4 h-4" />
                      Reject
                    </button>

                    <Link
                      href={`/candidate/${candidate.id}`}
                      className="inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium text-blue-600 hover:bg-blue-50"
                    >
                      View
                      <ArrowRight className="w-4 h-4" />
                    </Link>
                  </div>
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}