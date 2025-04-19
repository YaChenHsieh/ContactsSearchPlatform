'use client';

import { useState } from 'react';
import ResultTable from '@/components/ResultTable';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

console.log("API URL:", process.env.NEXT_PUBLIC_API_URL);


export default function Home() {
  const [formData, setFormData] = useState({
    company: '',
    position: '',
    role_type:'',
    location: '',
    school: '',
  });

  const [results, setResults] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSearch = async (role_type: string) => {
    setLoading(true);

    // call the API
    // const res = await fetch('http://localhost:8000/contacts/hunters', {
    const res = await fetch(`${API_BASE_URL}/contacts/hunters`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      // data pass to backend
      body: JSON.stringify({
        company: formData.company,
        position: formData.position,
        role_type:role_type, // role_type got from button
        location: formData.location,
        school: formData.school,
      }),
    });

    const data = await res.json();
    setResults(data);
    setLoading(false);
  };

  const handleAlumniSearch = async () => {
    setLoading(true);

    // call the API
    const res = await fetch(`${API_BASE_URL}/contacts/alumni`, {
    // const res = await fetch('http://localhost:8000/contacts/alumni', {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      // data pass to backend
      body: JSON.stringify({
        company: formData.company,
        position: formData.position,
        location: formData.location,
        school: formData.school,
      }),
    });
  
    const data = await res.json();
    setResults(data);
    setLoading(false);
  };

  return (
    <main className="p-6 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-6 text-center">🔍 LinkedIn Finder</h1>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
        <input
          name="company"
          placeholder="Company to search"
          value={formData.company}
          onChange={handleChange}
          className="border border-gray-300 rounded px-3 py-2 text-black"
        />
        <input
          name="position"
          placeholder="Job Title I am applying for"
          value={formData.position}
          onChange={handleChange}
          className="border border-gray-300 rounded px-3 py-2 text-black"
        />
        <input
          name="location"
          placeholder="Location I prefer"
          value={formData.location}
          onChange={handleChange}
          className="border border-gray-300 rounded px-3 py-2 text-black"
        />
        <input
          name="school"
          placeholder="School I went to"
          value={formData.school}
          onChange={handleChange}
          className="border border-gray-300 rounded px-3 py-2 text-black"
        />
      </div>

      <div className="flex flex-wrap gap-4 justify-center mb-6">
        {['CEO', 'Recruiter', 'PM', 'HR'].map((role_type) => (
          <button
            key={role_type}
            onClick={() => handleSearch(role_type)}
            className="bg-blue-500 text-white px-5 py-2 rounded hover:bg-blue-600"
          >
            {role_type}
          </button>
        ))}

        <button
            onClick={handleAlumniSearch}
            className="bg-purple-600 text-white px-5 py-2 rounded hover:bg-purple-700"
          >
            Alumni
          </button>
      </div>

      {loading ? (
        <p className="text-center text-gray-500">Loading...</p>
      ) : (
        results.length > 0 && (
          <table className="table-auto w-full border border-gray-300">
            <thead className="bg-gray-100">
              <tr>
                <th className="border px-4 py-2 text-black">Company</th>
                <th className="border px-4 py-2 text-black">Name</th>
                <th className="border px-4 py-2 text-black">LinkedIn</th>
              </tr>
            </thead>
            <tbody>
              {results.map((item, index) => (
                <tr key={index}>
                  <td className="border px-4 py-2">{item.company}</td>
                  <td className="border px-4 py-2">{item.name}</td>
                  <td className="border px-4 py-2">
                    <a
                      href={item.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-blue-600 underline"
                    >
                      LinkedIn
                    </a>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )
      )}
    </main>
  );
}
