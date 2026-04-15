from fastapi import FastAPI
from uuid import uuid4
from schemas import Issue
import database

app = FastAPI()


@app.get("/")
def home():
    return {"message": "My API is working!"}


# CREATE
@app.post("/issues")
def create_issue(issue: Issue):
    new_issue = issue.dict()
    new_issue["id"] = str(uuid4())
    new_issue["createdAt"] = str(__import__("datetime").datetime.utcnow())

    database.issues.append(new_issue)
    return new_issue


# READ ALL
@app.get("/issues")
def get_issues():
    return database.issues


# READ ONE
@app.get("/issues/{issue_id}")
def get_issue(issue_id: str):
    for issue in database.issues:
        if issue["id"] == issue_id:
            return issue
    return {"error": "Issue not found"}


# UPDATE
@app.put("/issues/{issue_id}")
def update_issue(issue_id: str, updated: Issue):
    for issue in database.issues:
        if issue["id"] == issue_id:
            issue["title"] = updated.title
            issue["description"] = updated.description
            issue["status"] = updated.status
            return issue
    return {"error": "Issue not found"}


# DELETE
@app.delete("/issues/{issue_id}")
def delete_issue(issue_id: str):
    for i, issue in enumerate(database.issues):
        if issue["id"] == issue_id:
            database.issues.pop(i)
            return {"message": "Issue deleted"}
    return {"error": "Issue not found"}