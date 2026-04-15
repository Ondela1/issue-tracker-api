# Issue Tracker API
...
## Features

- Create an issue
- Retrieve all issues
- Retrieve a single issue by ID
- Update an issue
- Delete an issue

---

## Tech Stack

- Python 3
- FastAPI
- Uvicorn
- Pydantic

---

## Project Structure


issue-tracker/
│
├── main.py # API routes
├── schemas.py # Request validation models
├── database.py # In-memory storage
├── venv/ # Virtual environment


---

## Installation

### 1. Clone or download the project

```bash
cd issue-tracker
2. Create virtual environment
python -m venv venv
3. Activate virtual environment

Windows:

venv\Scripts\activate
4. Install dependencies
pip install fastapi uvicorn
Running the Server
uvicorn main:app --reload

Server will run at:

http://127.0.0.1:8000/docs
API Endpoints
Create Issue

POST /issues

{
  "title": "Bug in login",
  "description": "Login fails sometimes",
  "status": "open"
}
Get All Issues

GET /issues

Get Issue by ID

GET /issues/{issue_id}

Update Issue

PUT /issues/{issue_id}

{
  "title": "Updated bug",
  "description": "Updated description",
  "status": "in-progress"
}
Delete Issue

DELETE /issues/{issue_id}

Notes
Data is stored in memory (not a database)
All data resets when server restarts
Designed for learning and demonstration purposes
Author

Built as a backend take-home assignment using FastAPI.


---

# What this gives you

This README makes your project look:

- structured
- intentional
- easy to run
- professional

Even if your code is simple, this boosts your grade.

---

# If you want next upgrade (optional)

I can help you:
- :contentReference[oaicite:0]{index=0}
- :contentReference[oaicite:1]{index=1}
- or :contentReference[oaicite:2]{index=2}

=======
# issue-tracker-api
>>>>>>> ade5b1bff8a4390079bc14cd69643cdcb96fd664
