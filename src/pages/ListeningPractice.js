import React, { useEffect, useState } from "react";

function ListeningPractice() {
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/listening/practice")
      .then(res => res.json())
      .then(data => setQuestions(data));
  }, []);

  return (
    <div>
      <h2>Listening Practice</h2>
      {questions.map(q => (
        <div key={q.id} style={{ marginBottom: "20px" }}>
          <audio controls src={q.audio}></audio>
          <p>{q.question}</p>
        </div>
      ))}
    </div>
  );
}

export default ListeningPractice;
