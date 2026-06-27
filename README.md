# 🛡️ SmartEscalate AI

> **Enterprise AI Governance Platform for Human-in-the-Loop Decision Making**

SmartEscalate AI is an enterprise AI governance platform that enables autonomous AI systems to safely escalate high-risk operations to a human decision-maker through an intelligent voice approval workflow.

Instead of blindly executing destructive or business-critical actions, SmartEscalate AI evaluates operational risk using a Human Decision Index (HDI), generates an executive business briefing with AI, and connects decision-makers through a real-time voice conversation before execution continues.

Built using **FastAPI**, **React**, **OpenAI**, and **VocalBridge AI**.

---

# 🚀 Overview

As AI systems become increasingly autonomous, they eventually reach decisions that should **not** be executed without human approval.

Examples include:

- Deleting production databases
- Deploying directly to production
- Rotating security credentials
- Restarting mission-critical services
- Executing irreversible infrastructure changes
- Performing high-impact customer operations

SmartEscalate AI acts as an intelligent governance layer between autonomous AI systems and human operators.

Instead of stopping with an error or waiting for someone to return to their keyboard, SmartEscalate AI:

1. Evaluates operational risk.
2. Calculates a Human Decision Index (HDI).
3. Generates an executive AI briefing.
4. Initiates a voice conversation.
5. Captures the human decision.
6. Returns the decision to the requesting AI system.

---

# 🎯 Problem Statement

Current autonomous AI systems are becoming increasingly capable, but they still struggle with decisions that involve:

- Business judgment
- Operational risk
- Security impact
- Customer impact
- Human accountability

Most systems simply stop and wait for manual intervention.

This interrupts productivity and creates unnecessary delays.

SmartEscalate AI introduces a structured Human-in-the-Loop workflow that allows AI systems to continue operating safely while involving humans only when required.

---

# 💡 Solution

SmartEscalate AI evaluates every high-risk request before deciding whether human intervention is necessary.

Instead of using simple rule-based logic, multiple operational factors are analyzed to calculate a Human Decision Index (HDI).

Only when the calculated risk exceeds the acceptable threshold does SmartEscalate AI initiate a voice approval session.

---

# ⭐ Key Features

## 🧠 Human Decision Index (HDI)

Calculates operational risk using multiple business and technical factors.

Examples include:

- Destructive operations
- Production environment
- Security impact
- Customer impact
- Business preference
- Architecture changes
- Rollback availability
- AI confidence

---

## 📋 AI Executive Briefing

Uses OpenAI to automatically generate:

- Executive Summary
- Business Risk
- Priority Justification
- Voice Briefing

allowing decision-makers to quickly understand the situation before approving an action.

---

## 🎙️ Voice Approval Workflow

When a high-risk operation is detected:

- AI pauses execution
- VocalBridge initiates a voice session
- The human hears a concise explanation
- The decision is captured through voice interaction

---

## ⚠️ Enterprise Risk Assessment

Every request receives:

- Human Decision Index
- Risk Priority
- Escalation Decision
- Executive Business Explanation

---

## 🌐 Modern Web Interface

The application includes a responsive React interface featuring:

- High-Risk Action Request form
- Human Decision Index visualization
- Executive Briefing
- Voice Session status
- Live conversation transcript

---

# 🏗️ System Architecture

```text
                 User Request
                      │
                      ▼
             React Frontend
                      │
                      ▼
              FastAPI Backend
                      │
                      ▼
         Human Decision Index Engine
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
 OpenAI Executive Briefing    Risk Assessment
        │                           │
        └─────────────┬─────────────┘
                      ▼
              Decision Service
                      │
                      ▼
          VocalBridge Voice Session
                      │
                      ▼
             Human Decision Maker
                      │
                      ▼
              Final Decision Returned
```

---

# 🧠 Human Decision Index (HDI)

SmartEscalate AI calculates a Human Decision Index before deciding whether human approval is required.

The score considers multiple operational factors.

| Factor | Purpose |
|---------|----------|
| Destructive Operation | Detect irreversible actions |
| Production Environment | Identify production risk |
| Security Impact | Evaluate security implications |
| Customer Impact | Measure business impact |
| Business Preference | Respect organizational policy |
| Architecture Change | Detect structural modifications |
| Rollback Availability | Determine recovery options |
| AI Confidence | Measure confidence in autonomous execution |

Higher scores indicate greater operational risk and increase the likelihood of requiring human approval.

---

# 📊 Decision Flow

```text
User submits request
        │
        ▼
Calculate Human Decision Index
        │
        ▼
Generate Executive Briefing
        │
        ▼
Determine Priority
        │
        ▼
Needs Human Approval?
      │             │
     No            Yes
      │             │
 Continue     Start Voice Session
                     │
                     ▼
             Human Decision
                     │
                     ▼
            Return Final Result
```
---

# 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Frontend | React.js |
| Backend | FastAPI |
| Programming Language | Python |
| AI Model | OpenAI GPT |
| Voice AI | VocalBridge AI |
| API Communication | REST APIs |
| Styling | CSS3 |
| Development Environment | VS Code |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```
SmartEscalate-AI/

│
├── backend/
│   │
│   ├── app/
│   │   │
│   │   ├── api/
│   │   │     └── routes.py
│   │   │
│   │   ├── core/
│   │   │     ├── config.py
│   │   │     └── hds_engine.py
│   │   │
│   │   ├── models/
│   │   │     ├── decision.py
│   │   │     └── voice_package.py
│   │   │
│   │   ├── services/
│   │   │     ├── decision_service.py
│   │   │     └── llm_service.py
│   │   │
│   │   ├── templates/
│   │   │     └── escalation_prompt.txt
│   │   │
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend/
│   │
│   ├── src/
│   │   │
│   │   ├── components/
│   │   │     ├── ActionInput.jsx
│   │   │     └── VoiceApproval.jsx
│   │   │
│   │   ├── services/
│   │   │     └── api.js
│   │   │
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── index.css
│   │
│   └── package.json
│
├── screenshots/
│
├── README.md
│
└── LICENSE
```

---

# ⚙️ Installation

## 1 Clone Repository

```bash
git clone https://github.com/Sifatkhan91/SmartEscalate-AI.git

cd SmartEscalate-AI
```

---

## 2 Backend Setup

```bash
cd backend

python -m venv .venv
```

Activate the virtual environment.

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## 3 Configure Environment Variables

Create a `.env` file.

```env
OPENAI_API_KEY=your_openai_api_key

OPENAI_MODEL=gpt-4.1-mini

VOCALBRIDGE_API_KEY=your_vocalbridge_api_key

VOCALBRIDGE_AGENT_ID=your_agent_id

VOCALBRIDGE_API_URL=https://api.vocalbridge.ai/api/v1/token
```

---

## 4 Start Backend

```bash
uvicorn app.main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 5 Frontend Setup

```bash
cd frontend

npm install
```

Start React.

```bash
npm run dev
```

Frontend:

```
http://localhost:5173
```

---

# 🌐 REST API

## Analyze High-Risk Action

```
POST /decision
```

Example Request

```json
{
  "action": "Delete Production Database",
  "reason": "Database corruption after failed migration",
  "environment": "Production",
  "requested_by": "DevOps Team",
  "destructive": true,
  "production": true,
  "customer_impact": true,
  "rollback_available": false,
  "confidence": 20
}
```

Example Response

```json
{
  "human_decision_index":95,
  "decision":"CALL_HUMAN",
  "priority":"HIGH",
  "requires_human":true
}
```

---

## Voice Token

```
GET /api/voice-token
```

Returns a VocalBridge authentication token for establishing a real-time voice session.

---

## Health Check

```
GET /health
```

Returns the service status.

---

# 🎙 Voice Workflow

```
Risky Request

        │

        ▼

Calculate HDI

        │

        ▼

Generate Executive Briefing

        │

        ▼

Connect VocalBridge

        │

        ▼

Human Voice Conversation

        │

        ▼

Approval / Rejection

        │

        ▼

Return Decision
```

---

# 🔒 Human Decision Index

The Human Decision Index combines multiple operational factors to determine whether human approval is required.

Current evaluation factors include:

- Destructive Operations
- Production Environment
- Security Impact
- Customer Impact
- Business Preference
- Architecture Changes
- Rollback Availability
- AI Confidence

These factors are combined to produce a normalized Human Decision Index that determines the overall operational risk level.

# 🎯 Example Use Cases

SmartEscalate AI can be integrated into enterprise AI workflows such as:

- Production deployment approval
- Infrastructure automation
- Cloud resource deletion
- Database administration
- Security operations
- DevOps automation
- Autonomous coding assistants
- AI operations (AIOps)
- Human-in-the-loop governance
- Enterprise change management

---

# 🚀 Future Roadmap

### Version 1.1

- Decision History
- SQLite Audit Log
- Human Approval Dashboard
- Approval Timeline

### Version 1.2

- Microsoft Teams Integration
- Slack Integration
- Email Notifications
- SMS Approval Workflow

### Version 2.0

- Multi-user Authentication
- RBAC (Role-Based Access Control)
- Enterprise Analytics
- Policy Engine
- Approval Policies
- Multi-Agent Support
- Kubernetes Deployment
- Cloud Deployment Templates

---

# 🏆 Competition Highlights

SmartEscalate AI demonstrates several modern AI engineering concepts:

✅ Human-in-the-Loop AI

✅ Explainable AI

✅ AI Governance

✅ AI Risk Assessment

✅ Voice AI

✅ FastAPI Backend

✅ React Frontend

✅ OpenAI Integration

✅ VocalBridge Integration

✅ Enterprise User Experience

---

# 🌟 Why SmartEscalate AI?

Modern AI systems are becoming increasingly autonomous.

However, autonomy without governance introduces operational risk.

SmartEscalate AI demonstrates how AI systems can remain autonomous while still involving humans at the right moments.

Rather than interrupting users unnecessarily, SmartEscalate AI evaluates operational risk and escalates only when human judgment is genuinely required.

This approach improves both safety and productivity while maintaining accountability.

---

# 🤝 Contributing

Contributions are welcome.

If you have ideas for improving SmartEscalate AI:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

See the **LICENSE** file for more information.

---

# 👨‍💻 Author

## Sifat Ullah Khan

**AI Engineer | Machine Learning Engineer | Microsoft Certified AI Engineer**

### Connect with me

**GitHub**

https://github.com/Sifatkhan91

**LinkedIn**

> Add your LinkedIn profile here

---

# 🙏 Acknowledgements

Special thanks to:

- OpenAI
- VocalBridge AI
- FastAPI
- React
- Microsoft
- The open-source AI community

for providing the technologies that made this project possible.

---

# ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 💡 Share your feedback
- 🤝 Connect on LinkedIn

Your support helps improve future AI engineering projects.

---

# 📬 Contact

For collaboration, consulting, or AI engineering opportunities:

**Sifat Ullah Khan**

AI Engineer

GitHub:

https://github.com/Sifatkhan91

LinkedIn:

www.linkedin.com/in/sifat-ullah-khan-34520746

---



# 🛡 SmartEscalate AI

### Enterprise AI Governance for Human-in-the-Loop Decision Making

**Built with ❤️ using FastAPI, React, OpenAI, and VocalBridge AI**

*"Autonomous AI is powerful. Governed AI is trustworthy."*