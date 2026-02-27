"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import {
  User,
  Briefcase,
  GraduationCap,
  Code2,
  Star,
} from "lucide-react";

export default function CandidateProfilePage() {
  const params = useParams();

  // ✅ resume_id from route
  const resume_id = params.slug

  const [candidate, setCandidate] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // ---------------- FETCH DATA (FIXED) ----------------
  useEffect(() => {
    if (!resume_id) return;

    console.log("Fetching resume:", resume_id);

    setLoading(true);

    fetch(`http://localhost:8080/api/candidate/${resume_id}`)
      .then((res) => {
        if (!res.ok) throw new Error("Candidate not found");
        return res.json();
      })
      .then((data) => {
        setCandidate(data);
        setError(null);
      })
      .catch((err) => {
        console.error(err);
        setError(err.message);
        setCandidate(null);
      })
      .finally(() => setLoading(false));
  }, [resume_id]);

  // ---------------- LOADING ----------------
// ---------- LOADING SKELETON ----------
if (loading) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 p-8">
      <div className="max-w-4xl mx-auto space-y-6 animate-pulse">
        <div className="h-28 rounded-2xl bg-gradient-to-r from-blue-200 via-blue-100 to-green-200" />
        <div className="h-24 rounded-2xl bg-white" />
        <div className="h-40 rounded-2xl bg-white" />
        <div className="h-32 rounded-2xl bg-white" />
      </div>
    </div>
  );
}
  // ---------------- ERROR ----------------
  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center text-red-600">
        {error}
      </div>
    );
  }

  if (!candidate) return null;

  // ---------------- UI ----------------
  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <div className="max-w-4xl mx-auto space-y-8">

        {/* HEADER CARD */}
        <div className="bg-white rounded-2xl p-6 shadow-sm flex justify-between items-center">
          <div className="flex items-center gap-4">
            <div className="w-14 h-14 rounded-full bg-blue-100 flex items-center justify-center">
              <User className="w-7 h-7 text-blue-600" />
            </div>
            <div>
              <h1 className="text-2xl font-semibold text-gray-900">
                {candidate.name}
              </h1>
              <p className="text-gray-600">{candidate.role}</p>
              <p className="text-xs text-gray-400">
                Resume ID: {candidate.id}
              </p>
            </div>
          </div>

          <div className="text-right">
            <p className="text-xs text-gray-500">AI Score</p>
            <p className="text-3xl font-bold text-green-600">
              {candidate.score}%
            </p>
          </div>
        </div>

        {/* SKILLS */}
        <section className="bg-white rounded-2xl p-6 shadow-sm">
          <h2 className="flex items-center gap-2 font-semibold mb-4">
            <Star className="w-5 h-5 text-blue-500" /> Skills
          </h2>
          <div className="flex flex-wrap gap-2">
            {candidate.skills?.map((skill) => (
              <span
                key={skill}
                className="px-3 py-1 rounded-full bg-blue-50 text-blue-700 text-sm"
              >
                {skill}
              </span>
            ))}
          </div>
        </section>

        {/* EXPERIENCE */}
        <section className="bg-white rounded-2xl p-6 shadow-sm">
          <h2 className="flex items-center gap-2 font-semibold mb-4">
            <Briefcase className="w-5 h-5 text-blue-500" /> Experience
          </h2>
          <div className="space-y-4">
            {candidate.experience?.map((exp, i) => (
              <div key={i}>
                <p className="font-medium text-gray-900">{exp.role}</p>
                <p className="text-sm text-gray-600">
                  {exp.company} • {exp.duration}
                </p>
                <p className="text-sm text-gray-500 mt-1">
                  {exp.description}
                </p>
              </div>
            ))}
          </div>
        </section>

        {/* EDUCATION */}
        <section className="bg-white rounded-2xl p-6 shadow-sm">
          <h2 className="flex items-center gap-2 font-semibold mb-4">
            <GraduationCap className="w-5 h-5 text-blue-500" /> Education
          </h2>
          <div className="space-y-3">
            {candidate.education?.map((edu, i) => (
              <div key={i}>
                <p className="font-medium text-gray-900">{edu.degree}</p>
                <p className="text-sm text-gray-600">
                  {edu.institute} • {edu.year}
                </p>
              </div>
            ))}
          </div>
        </section>

        {/* PROJECTS */}
        {candidate.projects?.length > 0 && (
          <section className="bg-white rounded-2xl p-6 shadow-sm">
            <h2 className="flex items-center gap-2 font-semibold mb-4">
              <Code2 className="w-5 h-5 text-blue-500" /> Projects
            </h2>
            <div className="space-y-4">
              {candidate.projects.map((p, i) => (
                <div key={i} className="border rounded-xl p-4">
                  <p className="font-medium text-gray-900">{p.name}</p>
                  <p className="text-sm text-gray-500 mt-1">
                    {p.description}
                  </p>
                </div>
              ))}
            </div>
          </section>
        )}

      </div>
    </div>
  );
}