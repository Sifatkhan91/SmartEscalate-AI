import "./App.css";
import VoiceApproval from "./components/VoiceApproval";

function App() {
    return (
        <div className="app">

            <header className="hero">

                <div className="hero-badge">
                    Enterprise AI Governance Platform
                </div>

                <h1>
                    🛡 SmartEscalate AI
                </h1>

                <p className="hero-text">

                    Human-in-the-Loop approval platform for autonomous AI systems.

                    SmartEscalate AI automatically evaluates operational,
                    security, and business risks before allowing high-impact
                    actions to proceed.

                </p>

            </header>

            <section className="overview">

                <div className="overview-card">

                    <div className="overview-icon">
                        🧠
                    </div>

                    <h3>
                        Human Decision Index
                    </h3>

                    <p>

                        Calculates the risk score for every autonomous action
                        using multiple business and technical factors.

                    </p>

                </div>

                <div className="overview-card">

                    <div className="overview-icon">
                        ⚠️
                    </div>

                    <h3>
                        AI Risk Assessment
                    </h3>

                    <p>

                        OpenAI generates an executive briefing explaining
                        business impact in clear language for decision makers.

                    </p>

                </div>

                <div className="overview-card">

                    <div className="overview-icon">
                        🎙️
                    </div>

                    <h3>
                        Voice Approval
                    </h3>

                    <p>

                        High-risk operations are paused until an authorized
                        human approves or rejects the action through voice.

                    </p>

                </div>

            </section>

            <VoiceApproval />

            <footer className="footer">

                <p>

                    SmartEscalate AI v1.0 • Enterprise AI Governance •
                    Human Approval Workflow

                </p>

            </footer>

        </div>
    );
}

export default App;