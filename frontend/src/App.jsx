import { useState } from "react";
import "./App.css";

function App() {
  const [mode, setMode] = useState("code"); // NEW
  const [code, setCode] = useState("def divide(a, b): return a / b");
  const [diff, setDiff] = useState("+ def divide(a, b):\n+     return a / b"); // NEW
  const [language, setLanguage] = useState("python");
  const [context, setContext] = useState("Simple function");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const review = async () => {
    setLoading(true);
    setResult(null);

    try {
      const endpoint =
        mode === "code"
          ? "http://127.0.0.1:8000/api/review"
          : "http://127.0.0.1:8000/api/review-diff";

      const body =
        mode === "code"
          ? { code, language, context }
          : { diff };

      const response = await fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
      });

      if (!response.ok) {
        const text = await response.text();
        throw new Error(text || "Request failed");
      }

      const data = await response.json();
      setResult(data);
    } catch (error) {
      setResult({ error: error.message });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <h1>AI Code Review Engine</h1>

      {/* MODE SWITCH */}
      <div style={{ marginBottom: "10px" }}>
        <button onClick={() => setMode("code")}>Code Review</button>
        <button onClick={() => setMode("diff")}>Diff Review</button>
      </div>

      {/* CODE MODE */}
      {mode === "code" && (
        <>
          <input
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
            placeholder="Language"
          />

          <input
            value={context}
            onChange={(e) => setContext(e.target.value)}
            placeholder="Context"
          />

          <textarea
            value={code}
            onChange={(e) => setCode(e.target.value)}
            rows={10}
          />
        </>
      )}

      {/* DIFF MODE */}
      {mode === "diff" && (
        <textarea
          value={diff}
          onChange={(e) => setDiff(e.target.value)}
          rows={10}
        />
      )}

      <button onClick={review} disabled={loading}>
        {loading ? "Reviewing..." : "Review"}
      </button>

      {result && (
        <pre className="result">
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  );
}

export default App;