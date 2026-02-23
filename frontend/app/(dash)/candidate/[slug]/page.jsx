"use client";

import { User, Briefcase, GraduationCap, Code2, Star } from "lucide-react";

// Dummy candidate data (replace with API data)
const candidate = {
  id: "cf-1021",
  name: "Arjun Menon",
  role: "Frontend Engineer",
  score: 92,
  skills: ["React", "Next.js", "JavaScript", "Tailwind CSS", "TypeScript"],
  experience: [
    {
      company: "Startup Labs",
      role: "Frontend Developer",
      duration: "2023 – 2024",
      description:
        "Built responsive dashboards and optimized frontend performance using React and Tailwind CSS.",
    },
  ],
  education: [
    {
      institute: "Muthoot Institute of Technology and Science",
      degree: "BTech Computer Science",
      year: "2022 – 2026",
    },
  ],
  projects: [
    {
      name: "AI Resume Parser",
      description:
        "Developed an AI-based resume parsing pipeline using Redis queues and NLP models.",
    },
    {
      name: "Campus Forge Engine",
      description:
        "Built an end-to-end candidate evaluation engine with scoring and job matching.",
    },
  ],
};

export default function CandidateProfilePage() {
  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <div className="max-w-5xl mx-auto space-y-8">
        {/* Header */}
        <div className="bg-white border rounded-2xl p-6 shadow-sm flex flex-col md:flex-row md:items-center md:justify-between gap-6">
          <div className="flex items-center gap-4">
            <div className="w-16 h-16 rounded-full bg-blue-100 flex items-center justify-center">
              <User className="w-8 h-8 text-blue-600" />
            </div>
            <div>
              <h1 className="text-2xl font-semibold text-gray-900">
                {candidate.name}
              </h1>
              <p className="text-gray-600">{candidate.role}</p>
              <p className="text-xs text-gray-500">Resume ID: {candidate.id}</p>
            </div>
          </div>

          <div className="text-right">
            <p className="text-sm text-gray-500">AI Match Score</p>
            <p className="text-3xl font-semibold text-green-600">
              {candidate.score}%
            </p>
          </div>
        </div>

        {/* Skills */}
        <section className="bg-white border rounded-2xl p-6 shadow-sm">
          <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <Star className="w-5 h-5 text-blue-500" /> Skills
          </h2>
          <div className="flex flex-wrap gap-2">
            {candidate.skills.map((skill) => (
              <span
                key={skill}
                className="px-3 py-1 rounded-full text-sm bg-blue-50 text-blue-700"
              >
                {skill}
              </span>
            ))}
          </div>
        </section>

        {/* Experience */}
        <section className="bg-white border rounded-2xl p-6 shadow-sm">
          <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <Briefcase className="w-5 h-5 text-blue-500" /> Experience
          </h2>
          <div className="space-y-4">
            {candidate.experience.map((exp, index) => (
              <div key={index}>
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

        {/* Education */}
        <section className="bg-white border rounded-2xl p-6 shadow-sm">
          <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <GraduationCap className="w-5 h-5 text-blue-500" /> Education
          </h2>
          <div className="space-y-3">
            {candidate.education.map((edu, index) => (
              <div key={index}>
                <p className="font-medium text-gray-900">{edu.degree}</p>
                <p className="text-sm text-gray-600">
                  {edu.institute} • {edu.year}
                </p>
              </div>
            ))}
          </div>
        </section>

        {/* Projects */}
        <section className="bg-white border rounded-2xl p-6 shadow-sm">
          <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <Code2 className="w-5 h-5 text-blue-500" /> Projects
          </h2>
          <div className="space-y-4">
            {candidate.projects.map((project, index) => (
              <div key={index}>
                <p className="font-medium text-gray-900">{project.name}</p>
                <p className="text-sm text-gray-500">
                  {project.description}
                </p>
              </div>
            ))}
          </div>
        </section>
      </div>
    </div>
  );
}
