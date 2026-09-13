import React, { useState, useRef } from "react";

function SpeakingPractice() {
  const [recording, setRecording] = useState(false);
  const [audioURL, setAudioURL] = useState("");
  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);

  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorderRef.current = new MediaRecorder(stream);
    audioChunksRef.current = [];

    mediaRecorderRef.current.ondataavailable = (event) => {
      audioChunksRef.current.push(event.data);
    };

    mediaRecorderRef.current.onstop = () => {
      const audioBlob = new Blob(audioChunksRef.current, { type: "audio/mp3" });
      const url = URL.createObjectURL(audioBlob);
      setAudioURL(url);

      // Upload to backend
      const formData = new FormData();
      formData.append("file", audioBlob, "response.mp3");

      fetch("http://localhost:5000/speaking/upload", {
        method: "POST",
        body: formData,
      }).then(res => res.json())
        .then(data => console.log("Uploaded:", data));
    };

    mediaRecorderRef.current.start();
    setRecording(true);
  };

  const stopRecording = () => {
    mediaRecorderRef.current.stop();
    setRecording(false);
  };

  return (
    <div>
      <h2>Speaking Practice</h2>
      <p>Prompt: Describe a memorable trip you have taken.</p>

      {!recording ? (
        <button onClick={startRecording}>Start Recording</button>
      ) : (
        <button onClick={stopRecording}>Stop Recording</button>
      )}

      {audioURL && (
        <div>
          <h3>Your Recording</h3>
          <audio controls src={audioURL}></audio>
        </div>
      )}
    </div>
  );
}

export default SpeakingPractice;
