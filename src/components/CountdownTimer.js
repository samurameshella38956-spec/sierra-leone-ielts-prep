import React, { useState, useEffect } from "react";

function CountdownTimer({ initialMinutes = 60, onTimeUp }) {
  const [timeLeft, setTimeLeft] = useState(initialMinutes * 60); // seconds

  useEffect(() => {
    if (timeLeft <= 0) {
      onTimeUp();
      return;
    }

    const timer = setInterval(() => {
      setTimeLeft(prev => prev - 1);
    }, 1000);

    return () => clearInterval(timer);
  }, [timeLeft, onTimeUp]);

  const formatTime = (seconds) => {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m}:${s < 10 ? "0" : ""}${s}`;
  };

  return (
    <div style={{ fontSize: "24px", fontWeight: "bold", margin: "10px 0" }}>
      ⏳ Time Remaining: {formatTime(timeLeft)}
    </div>
  );
}

export default CountdownTimer;
