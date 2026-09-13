import React, { useEffect, useState } from "react";

function ScholarshipUpdates() {
  const [scholarships, setScholarships] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/scholarship/updates")
      .then(res => res.json())
      .then(data => setScholarships(data));
  }, []);

  return (
    <div>
      <h2>Scholarship Updates</h2>
      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>Title</th>
            <th>Deadline</th>
            <th>Eligibility</th>
            <th>Apply Link</th>
          </tr>
        </thead>
        <tbody>
          {scholarships.map(s => (
            <tr key={s.id}>
              <td>{s.title}</td>
              <td>{s.deadline}</td>
              <td>{s.eligibility}</td>
              <td><a href={s.link} target="_blank" rel="noopener noreferrer">Apply</a></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default ScholarshipUpdates;
