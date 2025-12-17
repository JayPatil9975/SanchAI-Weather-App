import { useState } from "react";
import { sendMessage } from "./api";
import { Cloud, Loader2, Send } from "lucide-react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSend = async () => {
    if (!message.trim()) return;
    setLoading(true);
    setReply("");
    setError("");
    try {
      const response = await sendMessage(message);
      setReply(response);
    } catch (err) {
      setError("Unable to connect to server. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !loading) {
      handleSend();
    }
  };

  return (
    <div className="page">
      <div className="card">
        <div className="header">
          <Cloud className="icon" size={40} strokeWidth={1.5} />
          <h1 className="title">SanchAI Weather</h1>
          <p className="subtitle">Your intelligent weather companion</p>
        </div>

        <div className="input-group">
          <input
            className="input"
            type="text"
            placeholder="Ask about weather in any city..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={handleKeyDown}
            disabled={loading}
          />
          <button
            className="button"
            onClick={handleSend}
            disabled={loading || !message.trim()}
          >
            {loading ? (
              <Loader2 className="spin" size={20} />
            ) : (
              <Send size={20} />
            )}
          </button>
        </div>

        {reply && (
          <div className="response fade-in">
            <div className="response-label">Weather Report</div>
            {reply}
          </div>
        )}
        
        {error && (
          <div className="error fade-in">
            <strong>Error:</strong> {error}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;