import { useState } from "react";
import { useVocalBridge, useTranscript } from "@vocalbridgeai/react";
import ActionInput from "./ActionInput";
import { requestHumanApproval } from "../services/api";

function VoiceApproval() {
  const { connect, disconnect, state, error } = useVocalBridge();
  const { transcript } = useTranscript();
  const [loading, setLoading] = useState(false);
  const [decision, setDecision] = useState(null);

  const handleAnalyze = async (form) => {
    try {
      setLoading(true);
      const response = await requestHumanApproval({
        action: form.action,
        reason: form.reason,
        environment: form.environment,
        requested_by: form.requested_by,
        destructive: true,
        production: form.environment === "Production",
        customer_impact: true,
        rollback_available: false,
        confidence: 20,
      });
      setDecision(response);
      await connect();
    } catch (err) {
      console.error(err);
      alert("Unable to start SmartEscalate AI.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <ActionInput onAnalyze={handleAnalyze} loading={loading} />
      {decision && (
        <>
          <div className="card">
            <h2>📊 SmartEscalate AI Analysis</h2>
            <hr />
            <p><strong>Action</strong><br />{decision.action}</p>
            <p><strong>Reason</strong><br />{decision.reason}</p>
            <p><strong>Environment</strong><br />{decision.environment}</p>
            <p><strong>Requested By</strong><br />{decision.requested_by}</p>
            <hr />
            <div className="metric-card">
              <h3>Human Decision Index</h3>
              <div className="score">{decision.human_decision_index}%</div>
              <div className="progress">
                <div className="progress-fill" style={{width: `${decision.human_decision_index}%`}} />
              </div>
            </div>
            <br />
            <div className={`badge ${decision.priority.toLowerCase()}`}>{decision.priority}</div>
            <div className="decision-box">{decision.decision}</div>
          </div>

          <div className="card">
            <h2>📋 AI Executive Briefing</h2>
            <hr />
            <p><strong>Executive Summary</strong><br />{decision.voice_package.summary}</p>
            <p><strong>Business Risk</strong><br />{decision.voice_package.business_risk}</p>
            <p><strong>Priority Reason</strong><br />{decision.voice_package.priority_reason}</p>
          </div>

          <div className="card">
            <h2>🎙 Voice Session</h2>
            <hr />
            <p><strong>Connection Status</strong></p>
            <div className={`status-badge ${state==="connected"?"status-connected":"status-disconnected"}`}>
              {state==="connected"?"🟢 Connected":`🟠 ${state}`}
            </div>
            {error && <div className="error-box">{String(error)}</div>}
            {state==="connected" && <button onClick={disconnect}>Disconnect Voice Session</button>}
          </div>

          <div className="card">
            <h2>💬 Live Conversation</h2>
            <hr />
            {transcript.length===0 ? (
              <div className="waiting-box">Waiting for conversation...</div>
            ) : (
              <div className="chat-container">
                {transcript.map((item,index)=>(
                  <div key={index} className={`chat-row ${item.role==="user"?"user":"ai"}`}>
                    <div className={`chat-bubble ${item.role==="user"?"user-bubble":"ai-bubble"}`}>
                      <div className="chat-author">{item.role==="user"?"👤 You":"🤖 SmartEscalate AI"}</div>
                      <div className="chat-text">{item.text}</div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </>
      )}
    </div>
  );
}

export default VoiceApproval;
