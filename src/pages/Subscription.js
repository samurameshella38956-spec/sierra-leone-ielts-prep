import React, { useState } from "react";

function Subscription({ userId }) {
  const [status, setStatus] = useState("");

  const handleSubscribe = (method) => {
    fetch("http://localhost:5000/payment/subscribe", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId, method })
    })
      .then(res => res.json())
      .then(data => setStatus(data.message));
  };

  return (
    <div>
      <h2>Premium Plan - $50</h2>
      <p>Select a payment method:</p>
      <button onClick={() => handleSubscribe("OrangeMoney")}>Pay with Orange Money</button>
      <button onClick={() => handleSubscribe("Afrimoney")}>Pay with Afrimoney</button>
      {status && <p>{status}</p>}
    </div>
  );
}

export default Subscription;
