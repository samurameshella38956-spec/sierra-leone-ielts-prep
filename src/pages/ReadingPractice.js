import React, { useEffect, useState } from "react";

function ReadingPractice() {
  const [passages, setPassages] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/reading/practice")
      .then(res => res.json())
      .then(data => setPassages(data));
  }, []);

  return (
    <div>
      <h2>Reading Comprehension Practice</h2>
      {passages.map(p => (
        <div key={p.id} style={{ marginBottom: "30px" }}>
          <h3>{p.title}</h3>
          <p>{p.passage}</p>
          <strong>Question:</strong> <p>{p.question}</p>
        </div>
      ))}
    </div>
  );
}

export default ReadingPractice;
