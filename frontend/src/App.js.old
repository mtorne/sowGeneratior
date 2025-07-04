import logo from './logo.svg';
import './App.css';

import React, { useState } from "react";
import axios from "axios";

function App() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async () => {
    setResponse("Generant resposta...");
    try {
      const res = await axios.post("http://89.168.92.241:8000/generatechat", {
        prompt,
      });
      setResponse(res.data.response);
    } catch (err) {
      setResponse("Error en la generació.");
      console.error(err);
    }
  };

  return (
    <div style={{ padding: "2rem", maxWidth: "600px", margin: "auto" }}>
      <h1>🤖 Generador d'IA OCI</h1>
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        rows={5}
        style={{ width: "100%", marginBottom: "1rem" }}
        placeholder="Escriu la teva pregunta o prompt aquí..."
      />
      <button onClick={handleSubmit}>Genera resposta</button>
      <div style={{ marginTop: "2rem", whiteSpace: "pre-wrap" }}>
        <strong>Resposta:</strong>
        <p>{response}</p>
      </div>
    </div>
  );
}

export default App;



