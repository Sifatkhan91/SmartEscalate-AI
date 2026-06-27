import { useState } from "react";

function ActionInput({ onAnalyze, loading }) {
    const [form, setForm] = useState({
        action: "",
        reason: "",
        environment: "Production",
        requested_by: "",
    });

    const handleChange = (e) => {
        setForm({
            ...form,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        if (!form.action.trim()) {
            alert("Please enter a risky action.");
            return;
        }

        if (!form.reason.trim()) {
            alert("Please enter the business reason.");
            return;
        }

        if (!form.requested_by.trim()) {
            alert("Please enter who requested this action.");
            return;
        }

        onAnalyze(form);
    };

    return (
        <div className="card">

            <h2>⚠️ High-Risk Action Request</h2>

            <hr />

            <form onSubmit={handleSubmit}>

                <label>
                    Risky Action
                </label>

                <input
                    type="text"
                    name="action"
                    value={form.action}
                    onChange={handleChange}
                    placeholder="Delete Production Database"
                />

                <label>
                    Business Reason
                </label>

                <textarea
                    name="reason"
                    value={form.reason}
                    onChange={handleChange}
                    rows={4}
                    placeholder="Database corruption detected after a failed production migration."
                />

                <label>
                    Environment
                </label>

                <select
                    name="environment"
                    value={form.environment}
                    onChange={handleChange}
                >
                    <option>Development</option>
                    <option>Testing</option>
                    <option>Staging</option>
                    <option>Production</option>
                </select>

                <label>
                    Requested By
                </label>

                <input
                    type="text"
                    name="requested_by"
                    value={form.requested_by}
                    onChange={handleChange}
                    placeholder="DevOps Team"
                />

                <div
                    style={{
                        marginTop: "25px",
                        padding: "18px",
                        borderRadius: "12px",
                        background: "rgba(59,130,246,.08)",
                        border: "1px solid rgba(59,130,246,.25)",
                    }}
                >

                    <strong
                        style={{
                            color: "#60a5fa",
                        }}
                    >
                        AI Governance Notice
                    </strong>

                    <p
                        style={{
                            marginTop: "10px",
                            fontSize: "14px",
                            lineHeight: "1.6",
                            color: "#cbd5e1",
                        }}
                    >
                        SmartEscalate AI will calculate the Human Decision Index,
                        evaluate operational and business risk, generate an executive
                        briefing, and initiate a voice approval workflow if human
                        authorization is required.
                    </p>

                </div>

                <button
                    type="submit"
                    disabled={loading}
                >
                    {loading
                        ? "Analyzing Risk..."
                        : "🚀 Analyze & Start Voice Approval"}
                </button>

            </form>

        </div>
    );
}

export default ActionInput;