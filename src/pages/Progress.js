import React, { useEffect, useState } from "react";

function Progress({ token }) {
  const [progress, setProgress] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/auth/progress", {
      headers: { Authorization: `Bearer ${token}` }
    })
      .then(res => res.json())
      .then(data => setProgress(data));
  }, [token]);

  return (
    <div>
      <h2>Your Progress</h2>
      <ul>
        {progress.map((p, i) => (
          <li key={i}>{p.exam_type}: {p.score}</li>
        ))}
      </ul>
    </div>
  );
}

export default Progress;
