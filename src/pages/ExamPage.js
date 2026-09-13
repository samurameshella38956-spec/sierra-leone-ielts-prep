import React, { useEffect, useState } from "react";

function ExamPage() {
  const [exam, setExam] = useState(null);

  useEffect(() => {
    fetch("http://localhost:5000/exam/mock")
      .then(res => res.json())
      .then(data => setExam(data));
  }, []);

  if (!exam) return <p>Loading exam...</p>;

  return (
    <div>
      <h2>IELTS Mock Exam</h2>

      <section>
        <h3>Listening</h3>
        {exam.listening.map(q => (
          <div key={q.id}>
            <audio controls src={q.audio}></audio>
            <p>{q.question}</p>
          </div>
        ))}
      </section>

      <section>
        <h3>Reading</h3>
        {exam.reading.map(q => (
          <div key={q.id}>
            <p><strong>Passage:</strong> {q.passage}</p>
            <p>{q.question}</p>
          </div>
        ))}
      </section>

      <section>
        <h3>Writing</h3>
        {exam.writing.map(q => (
          <div key={q.id}>
            <p>{q.task}</p>
          </div>
        ))}
      </section>

      <section>
        <h3>Speaking</h3>
        {exam.speaking.map(q => (
          <div key={q.id}>
            <p>{q.prompt}</p>
          </div>
        ))}
      </section>
    </div>
  );
}

export default ExamPage;
