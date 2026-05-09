from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os
import json
import re
import requests

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class SearchInput(BaseModel):
    skills: str
    experience: str

GITHUB_HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "opencontrib-app"
}

def get_difficulty(stars, open_issues):
    if stars < 500 and open_issues > 5:
        return "Beginner"
    elif stars < 5000:
        return "Intermediate"
    else:
        return "Advanced"

def search_github_repos(skills):
    skill_list = [s.strip() for s in skills.split(",")]
    query = "+".join(skill_list) + "+good-first-issues:>3"
    url = f"https://api.github.com/search/repositories?q={query}&sort=updated&per_page=9"
    
    response = requests.get(url, headers=GITHUB_HEADERS)
    if response.status_code != 200:
        return []
    
    data = response.json()
    repos = []
    
    for repo in data.get("items", []):
        repos.append({
            "name": repo["name"],
            "full_name": repo["full_name"],
            "description": repo["description"] or "No description available",
            "stars": repo["stargazers_count"],
            "language": repo["language"] or "Various",
            "open_issues": repo["open_issues_count"],
            "url": repo["html_url"],
            "issues_url": repo["html_url"] + "/issues?q=is%3Aopen+label%3A%22good+first+issue%22",
            "difficulty": get_difficulty(repo["stargazers_count"], repo["open_issues_count"])
        })
    
    return repos

@app.get("/")
def home():
    return {"status": "OpenContrib is running"}

@app.post("/search")
def search_projects(input: SearchInput):
    repos = search_github_repos(input.skills)
    
    if not repos:
        return {
            "repos": [],
            "ai_suggestion": "No repos found. Try different skills like: python, javascript, react"
        }
    
    repo_summary = "\n".join([
        f"- {r['name']} ({r['language']}, {r['stars']} stars, {r['open_issues']} open issues, difficulty: {r['difficulty']})"
        for r in repos[:5]
    ])
    
    prompt = f"""
A developer with these skills: {input.skills}
Experience level: {input.experience}

Found these open source projects:
{repo_summary}

Give a short 2-3 sentence personalised recommendation on which project they should contribute to first and why.
Also give one specific tip on what kind of issue to look for as a first contribution.
Keep it friendly and encouraging. Plain text only, no markdown.
"""
    
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
        )
        ai_suggestion = response.choices[0].message.content.strip()
    except:
        ai_suggestion = "Start with the beginner-friendly repos shown below. Look for issues labelled 'good first issue' or 'documentation'."
    
    return {
        "repos": repos,
        "ai_suggestion": ai_suggestion
    }