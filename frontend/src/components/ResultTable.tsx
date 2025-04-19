// src/components/ResultTable.tsx
'use client';

import React from 'react';

type ResultItem = {
  company: string;
  name: string;
  link: string;
};

type Props = {
  results: ResultItem[];
};

export default function ResultTable({ results }: Props) {
  return (
    <table className="table-auto w-full border border-gray-300">
      <thead className="bg-gray-100">
        <tr>
          <th className="border px-4 py-2">Company</th>
          <th className="border px-4 py-2">Name</th>
          <th className="border px-4 py-2">LinkedIn</th>
        </tr>
      </thead>
      <tbody>
        {results.map((item, index) => (
          <tr key={index}>
            <td className="border px-4 py-2">{item.company}</td>
            <td className="border px-4 py-2">{item.name}</td>
            <td className="border px-4 py-2">
              <a
                href={item.link}
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
  );
}
