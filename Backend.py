# hackmate_backend.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import openai  # OpenAI API for AI generation
import random
import datetime

app = FastAPI(title="HackMate AI Backend")

# ----------------------
# Models
# ----------------------
class TeamInput(BaseModel):
    team_name: str
    members: List[str]
    skills: List[str]
    hackathon_theme: str

class HackathonRules(BaseModel):
    rules_text: str

class SimulationInput(BaseModel):
    team_name: str
    strategy: Dict[str, str]  # task: member
    time_remaining: int  # in hours

# ----------------------
# Config (set your API key in env)
# ----------------------
openai.api_key = "YOUR_OPENAI_API_KEY"

# ----------------------
# 1. Rule Extraction
# ----------------------
@app.post("/extract_rules")
def extract_rules(rules: HackathonRules):
    """
    Extract key rules and constraints from hackathon guidelines using OpenAI API
    """
    try:
        prompt = f"Extract key rules and deliverables from this text:\n{rules.rules_text}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role":"user","content":prompt}],
            max_tokens=500
        )
        rules_summary = response.choices[0].message.content
        return {"rules_summary": rules_summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ----------------------
# 2. Idea Generation
# ----------------------
@app.post("/generate_idea")
def generate_idea(team: TeamInput):
    """
    Generate hackathon project idea based on theme and skills
    """
    try:
        prompt = f"Suggest an innovative hackathon project idea for theme '{team.hackathon_theme}' using skills {team.skills}. Provide feasibility, estimated tasks, and tech stack."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role":"user","content":prompt}],
            max_tokens=500
        )
        idea = response.choices[0].message.content
        return {"project_idea": idea}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ----------------------
# 3. Simulation Engine
# ----------------------
@app.post("/simulate_hackathon")
def simulate_hackathon(sim: SimulationInput):
    """
    Simulate hackathon scenarios: random events affecting team progress
    """
    events = [
        "API outage", "Team member unavailable", "Unexpected bug", "Tech stack delay"
    ]
    random_event = random.choice(events)
    performance_score = random.randint(70, 95)  # mock performance score
    time_remaining = sim.time_remaining - random.randint(1, 3)
    return {
        "random_event": random_event,
        "updated_time_remaining": time_remaining,
        "performance_score": performance_score
    }

# ----------------------
# 4. Compliance Checker
# ----------------------
@app.post("/check_compliance")
def check_compliance(rules: HackathonRules, strategy: Dict[str,str]):
    """
    Compare strategy/tasks with extracted rules to flag violations
    """
    # Simple placeholder logic for demonstration
    violations = []
    if "pre-built code" in rules.rules_text.lower():
        for task, member in strategy.items():
            if "copy" in task.lower():
                violations.append(f"Task '{task}' may violate rule against pre-built code")
    return {"violations": violations, "is_compliant": len(violations) == 0}

# ----------------------
# 5. Output / Feedback
# ----------------------
@app.post("/generate_feedback")
def generate_feedback(team: TeamInput, strategy: Dict[str,str]):
    """
    Provide AI feedback on team strategy
    """
    prompt = f"Evaluate this team strategy: {strategy} for team with skills {team.skills} and theme '{team.hackathon_theme}'. Suggest improvements."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}],
        max_tokens=300
    )
    feedback = response.choices[0].message.content
    return {"feedback": feedback}

# ----------------------
# Health Check
# ----------------------
@app.get("/health")
def health_check():
    return {"status": "HackMate AI backend is running ✅", "time": datetime.datetime.now()}