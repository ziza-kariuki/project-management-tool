# 📂 Python Python Management CLI Tool 

A Python-based Command-Line Interface (CLI) application that manages a simulated multi-user project tracker system. 

## Features

*   **User Registration:** Create user profiles 
*   **Python Creation:** Add projects unique to each user
*   **Python Tracking:** Append smaller tasks to a project pending completion
*   **Data Storage:**  All user and project info is stores locally for future reference
*   **Dashboard View:** Renders neat tables of active projects and user profiles
*   **Automated Testing:** Local tests are available to verify the functionality of the code with further updates


## How to Run the project
### 1. Initialize Virtual Environment & Dependencies
a. Create the environment folder
```bash
python3 -m venv venv
```

b. Activate the local scope environment
```bash
source venv/bin/activate
```

c. Install the styling framework
```bash
pip install tabulate
```

### 2. Running CLI commands(examples)
a.To Register a User Profile:
```bash
python main.py add-user --name "Ziza Kariuki" --email "ziza@email.com"
```

b.To list all users:
```bash
python main.py list-users
```

c.To create a new project:
```bash
python main.py add-project --title "Python" --description "Developping command line interface" --due-date "2026-20-07"
```

d.To append a task to the project:
```bash
python main.py add-task --project "Python" --title "Write Unit Tests" --assigned-to "ziza@email.com"
```

e. Mark a task as complete:
```bash
python main.py complete-task --project "Python" --task "Write Unit Tests"
```

f. View Dashboard:
```bash
python main.py list-projects
```

### 3.Running automated tests
a. To execute the test suite,run:
```bash
python -m unittest discover -s tests -p "*.py"
```

## Technologies Used
Language: Python 3.12

External Packages: tabulate (v0.10.0)

Internal Modules: json, os, argparse, unittest
