import React, { useState } from "react";

function WritingFeedback() {
  const [essay, setEssay] = useState("");
  const [feedback, setFeedback] = useState("");

  const handleSubmit = () => {
    fetch("http://localhost:5000/writing-feedback/evaluate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ essay })
    })
      .then(res => res.json())
      .then(data => setFeedback(data.feedback));
  };

  return (
    <div>
      <h2>AI-Powered Writing Feedback</h2>
      <textarea
        rows="10"
        cols="70"
        value={essay}
        onChange={(e) => setEssay(e.target.value)}
        placeholder="Paste your IELTS essay here..."
      />
      <br />
      <button onClick={handleSubmit}>Get Feedback</button>

      {feedback && (
        <div style={{ marginTop: "20px" }}>
          <h3>Feedback</h3>
          <p>{feedback}</p>
        </div>
      )}
    </div>
  );
}

export default WritingFeedback;
