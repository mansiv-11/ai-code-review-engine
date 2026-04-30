import { useState } from "react";
import "./App.css";

function App() {
  const [code, setCode] = useState("def divide(a, b): return a / b");
  const [language, setLanguage] = useState("python");
  const [context, setContext] = useState("Simple function");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const reviewCode = async () => {
    setLoading(true);
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/api/review", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ code, language, context }),
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(errorText || "Request failed");
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
      <p>Review code for bugs, security risks, and improvements.</p>

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

      <button onClick={reviewCode} disabled={loading}>
        {loading ? "Reviewing..." : "Review Code"}
      </button>

      {result && !result.error && (
        <div className="results">
          {["bugs", "security", "improvements"].map((section) => (
            <div key={section} className="section">
              <h2>{section.toUpperCase()}</h2>

              {result[section]?.length === 0 ? (
                <p>No issues</p>
              ) : (
                result[section]?.map((item, idx) => (
                  <div key={idx} className="card">
                    <h3>{item.title}</h3>
                    <p>
                      <strong>Severity:</strong> {item.severity}
                    </p>
                    <p>{item.explanation}</p>
                    <p>
                      <strong>Fix:</strong> {item.suggestion}
                    </p>
                  </div>
                ))
              )}
            </div>
          ))}
        </div>
      )}

      {result?.error && <div className="error">{result.error}</div>}
    </div>
  );
}

export default App;