import json
import os
from models.user import User
from models.project import Project

DATA_FILE = "data.json"

def save_data(users: list, projects: list):
   #Saves system state to a local JSON file."
    dir_name = os.path.dirname(DATA_FILE)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    
    payload = {
        "users": [u.to_dict() for u in users],
        "projects": [p.to_dict() for p in projects]
    }
    
    with open(DATA_FILE, "w") as f:
        json.dump(payload, f, indent=4)


def load_data():
   #Loads system data
    users = []
    projects = []
    
    if not os.path.exists(DATA_FILE):
        return users, projects

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            
            # Reconstruct User objects
            for u_data in data.get("users", []):
                users.append(User.from_dict(u_data))
                
            # Reconstruct Project objects
            for p_data in data.get("projects", []):
                projects.append(Project.from_dict(p_data))
                
    except (json.JSONDecodeError, KeyError, TypeError):
        print("[Warning] Storage file was corrupted. Starting fresh.")
        
    return users, projects