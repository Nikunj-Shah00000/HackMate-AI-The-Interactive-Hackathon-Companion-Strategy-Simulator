

# HackMate AI – Interactive Hackathon Companion & Strategy Simulator

**HackMate AI** is a gamified web application that helps student teams prepare for hackathons like **BuildWithAI**. It simulates the hackathon journey, checks rule compliance, and generates personalized success strategies using AI-powered tools.

---

## 🔹 Features

* **AI-Powered Idea Generation** – Generate innovative project ideas based on team skills and hackathon themes.
* **Hackathon Simulation Engine** – Mimic real hackathon challenges with random events and performance scoring.
* **Rule Compliance Checker** – Ensure your strategy and tasks adhere to hackathon guidelines.
* **Personalized Feedback** – Receive actionable AI suggestions to optimize your plan.
* **Team Strategy Optimization** – Suggest task allocation based on member skills.

---

## 🛠 Technology Stack

* **Backend:** Python, FastAPI
* **AI & NLP:** OpenAI GPT-4, HuggingFace models, LangChain
* **Database:** (Optional) MongoDB / PostgreSQL for persistence
* **Frontend (Optional):** React / Vue.js
* **Deployment:** Local / Cloud (AWS, GCP, or Heroku)

---

## 📦 Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/<username>/HackMate-AI.git
cd HackMate-AI
```

2. Install dependencies:

```bash
pip install fastapi uvicorn openai pydantic
```

3. Set your OpenAI API key in environment variables:

```bash
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

4. Run the backend server:

```bash
uvicorn hackmate_backend:app --reload
```

5. Test endpoints at: `http://127.0.0.1:8000/docs` (Swagger UI)

---

## 🔗 API Endpoints

| Endpoint              | Method | Description                                 |
| --------------------- | ------ | ------------------------------------------- |
| `/extract_rules`      | POST   | Extract key rules from hackathon guidelines |
| `/generate_idea`      | POST   | Generate AI-powered project ideas           |
| `/simulate_hackathon` | POST   | Simulate hackathon events and scoring       |
| `/check_compliance`   | POST   | Check strategy against hackathon rules      |
| `/generate_feedback`  | POST   | AI feedback on team strategy                |
| `/health`             | GET    | Check backend health status                 |

---

## 📋 Hackathon Guidelines Compliance

* Entire project developed **within hackathon 24-hour window**.
* Uses **allowed AI platforms**: OpenAI, HuggingFace, LangChain, etc.
* **No pre-built projects or previously developed code** used.
* GitHub repository contains **commit history and modular code**.
* Properly **documents system architecture, workflow, and AI integration**.

---

## 🧠 System Workflow

1. **User Input:** Team details + hackathon theme + rules
2. **Rule Extraction:** NLP parses key rules
3. **Idea Generation:** AI suggests project ideas with feasibility
4. **Strategy Planning:** Assign tasks and create roadmap
5. **Simulation:** Run hackathon scenarios with random events
6. **Compliance Check:** Validate strategy against rules
7. **Feedback:** AI generates actionable improvements

---

## 📌 Contribution

* Contributions are welcome!
* Please follow **Python best practices** and document changes.
* Ensure **all code adheres to hackathon rules**.

---

## 📜 License

This project is for **educational and hackathon purposes only**.
All AI APIs and libraries used comply with their respective licenses.

---

## 📷 Screenshot / Demo 

> See Source code.

---

## 🎯 Contact

**HackMate AI Team**

* GitHub: https://github.com/Nikunj-Shah00000/HackMate-AI-The-Interactive-Hackathon-Companion-Strategy-Simulator
* Email: nikunjshah0310@gmail.com
