import React from "react";
import CountdownTimer from "../components/CountdownTimer";

function ExamPage() {
  const handleTimeUp = () => {
    alert("Time is up! Submitting your exam...");
    // Call backend submit endpoint here
    fetch("http://localhost:5000/exam/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ answers: "user answers here" })
    });
  };

  return (
    <div>
      <h2>IELTS Mock Exam</h2>
      <CountdownTimer initialMinutes={60} onTimeUp={handleTimeUp} />
      {/* Exam questions go here */}
    </div>
  );
}

export default ExamPage;
