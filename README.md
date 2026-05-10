# 🌐 OpenContrib

> Discover open source projects that match your skills. Find good first issues. Make your first contribution today.

## 🔗 Live Demo

**[https://opencontrib.netlify.app](https://opencontrib.netlify.app)**

## ✨ Features

- 🎯 Click-to-select skill tags — Python, ML, React, FastAPI and more
- 🔍 Real GitHub projects fetched live using GitHub public API
- 🤖 AI-powered personalised recommendations via Groq LLaMA 3.1
- 📊 Difficulty ratings — Beginner, Intermediate, Advanced
- ⭐ Star counts and open issue counts for every project
- 🔽 Filter by difficulty, sort by stars or issues
- 🚀 Direct links to good first issues on each project

## 🛠 Tech Stack

| Layer      | Technology                  |
|------------|-----------------------------|
| Backend    | Python, FastAPI             |
| AI         | Groq API — LLaMA 3.1        |
| Data       | GitHub Public API           |
| Frontend   | HTML, CSS, JavaScript       |
| Deployment | Render, Netlify             |

## 🚀 Run Locally

### Backend

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

### Frontend

Open `frontend/index.html` with Live Server in VS Code.

## 📁 Project Structure

```
opencontrib/
├── backend/
│   ├── main.py            # FastAPI + GitHub API + Groq AI
│   └── requirements.txt   # Python dependencies
├── frontend/
│   └── index.html         # UI with animations and filters
└── README.md
```

## 👨‍💻 Author

Built by **Enosh** — IT undergrad at Vasavi College of Engineering, Hyderabad

[![GitHub](https://img.shields.io/badge/GitHub-enoshdev-181717?style=flat&logo=github)](https://github.com/enoshdev)