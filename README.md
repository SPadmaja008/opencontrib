# OpenContrib

> Discover open source projects that match your skills. 
> Find good first issues. Make your first contribution today.

## Live Demo
[Link after deployment]

## Screenshot
[Add screenshot after deployment]

## What It Does
- Select your skills from a visual tag picker
- Get real GitHub projects fetched live using GitHub API
- See difficulty ratings, star counts, and open issue counts
- Get AI-powered personalised project recommendations
- Filter by difficulty and sort by stars or issues
- Direct links to good first issues on each project

## Tech Stack
- **Backend:** Python, FastAPI, GitHub Public API, Groq API
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render (backend) + Netlify (frontend)

## Run Locally

### Backend
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

### Frontend
Open frontend/index.html with Live Server in VS Code.

## Author
Built by Enosh — [github.com/enoshdev](https://github.com/enoshdev)