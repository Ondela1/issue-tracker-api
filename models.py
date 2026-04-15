from datetime import datetime

def create_issue_object(title, description, status):
    return {
        "title": title,
        "description": description,
        "status": status,
        "id": None,
        "createdAt": datetime.utcnow()
    }