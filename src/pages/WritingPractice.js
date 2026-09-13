import React, { useEffect, useState } from "react";

function WritingPractice() {
  const [tasks, setTasks] = useState({});
  const [response, setResponse] = useState("");

  useEffect(() => {
    fetch("http://localhost:5000/writing/practice")
      .then(res => res.json())
      .then(data => setTasks(data));
  }, []);

  const handleSubmit = (taskId) => {
    fetch("http://localhost:5000/writing/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ task_id: taskId, response })
    })
      .then(res => res.json())
      .then(data => alert(data.message));
  };

  return (
    <div>
      <h2>Writing Practice</h2>

      {Object.values(tasks).map(task => (
        <div key={task.id} style={{ marginBottom: "30px" }}>
          <h3>{task.type}</h3>
          <p>{task.prompt}</p>
          <textarea
            rows="6"
            cols="60"
            value={response}
            onChange={(e) => setResponse(e.target.value)}
          />
          <br />
          <button onClick={() => handleSubmit(task.id)}>Submit</button>
        </div>
      ))}
    </div>
  );
}

export default WritingPractice;
