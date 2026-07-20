import argparse
from tabulate import tabulate

from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import load_data, save_data

def handle_add_user(args, users, projects):
    # Check if user email already exists
    if any(u.email == args.email for u in users):
        print(f"❌ Error: A user with email '{args.email}' already exists.")
        return
    
    try:
        new_user = User(name=args.name, email=args.email)
        users.append(new_user)
        save_data(users, projects)
        print(f"✅ Successfully created user: {new_user}")
    except ValueError as e:
        print(f"❌ Error: {e}")

def handle_list_users(args, users, projects):
    if not users:
        print("ℹ️ No users registered yet.")
        return
    
    table_data = [[u.name, u.email] for u in users]
    print("\n👥 REGISTERED USERS")
    print(tabulate(table_data, headers=["Name", "Email"], tablefmt="grid"))

def handle_add_project(args, users, projects):
    if any(p.title.lower() == args.title.lower() for p in projects):
        print(f"❌ Error: A project named '{args.title}' already exists.")
        return

    new_project = Project(title=args.title, description=args.description, due_date=args.due_date)
    projects.append(new_project)
    save_data(users, projects)
    print(f"✅ Successfully created project: '{new_project.title}' (Due: {new_project.due_date})")

def handle_add_task(args, users, projects):
    # Find the target project
    project = next((p for p in projects if p.title.lower() == args.project.lower()), None)
    if not project:
        print(f"❌ Error: Project '{args.project}' not found.")
        return

    # Verify the assigned user exists
    if not any(u.email == args.assigned_to for u in users):
        print(f"❌ Error: Cannot assign task. User email '{args.assigned_to}' does not exist.")
        return

    new_task = Task(title=args.title, assigned_to=args.assigned_to)
    project.add_task(new_task)
    save_data(users, projects)
    print(f"✅ Task '{args.title}' added to Project '{project.title}' and assigned to {args.assigned_to}.")

def handle_complete_task(args, users, projects):
    project = next((p for p in projects if p.title.lower() == args.project.lower()), None)
    if not project:
        print(f"❌ Error: Project '{args.project}' not found.")
        return

    task = next((t for t in project.tasks if t.title.lower() == args.task.lower()), None)
    if not task:
        print(f"❌ Error: Task '{args.task}' not found in project '{project.title}'.")
        return

    task.mark_complete()
    save_data(users, projects)
    print(f"✅ Task '{task.title}' marked as Complete!")

def handle_list_projects(args, users, projects):
    if not projects:
        print("ℹ️ No projects found.")
        return

    print("\n📂 PROJECT MANAGEMENT DASHBOARD")
    for proj in projects:
        print(f"\n🚀 {proj.title.upper()} | Due: {proj.due_date}")
        print(f"📝 Description: {proj.description}")
        
        if proj.tasks:
            task_table = [[t.title, t.assigned_to, t.status] for t in proj.tasks]
            print(tabulate(task_table, headers=["Task Title", "Assigned To", "Status"], tablefmt="simple"))
        else:
            print("   (No tasks assigned to this project yet)")
        print("-" * 50)

def main():
    # Load state from file storage
    users, projects = load_data()

    parser = argparse.ArgumentParser(description="Python Project Management CLI Tool")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available subcommands")

    # Command: add-user
    parser_user = subparsers.add_parser("add-user", help="Register a new user account")
    parser_user.add_argument("--name", required=True, help="Full name of the user")
    parser_user.add_argument("--email", required=True, help="Unique email address")
    parser_user.set_defaults(func=handle_add_user)

    # Command: list-users
    parser_l_users = subparsers.add_parser("list-users", help="List all users")
    parser_l_users.set_defaults(func=handle_list_users)

    # Command: add-project
    parser_proj = subparsers.add_parser("add-project", help="Create a new workspace project")
    parser_proj.add_argument("--title", required=True, help="Unique project title")
    parser_proj.add_argument("--description", required=True, help="Short summary of project scope")
    parser_proj.add_argument("--due-date", required=True, help="Target delivery date (e.g., YYYY-MM-DD)")
    parser_proj.set_defaults(func=handle_add_project)

    # Command: add-task
    parser_task = subparsers.add_parser("add-task", help="Append a new milestone task to a project")
    parser_task.add_argument("--project", required=True, help="Title of the target project")
    parser_task.add_argument("--title", required=True, help="Specific name of the action item")
    parser_task.add_argument("--assigned-to", required=True, help="Assignee user email address")
    parser_task.set_defaults(func=handle_add_task)

    # Command: complete-task
    parser_comp = subparsers.add_parser("complete-task", help="Resolve and complete an outstanding task")
    parser_comp.add_argument("--project", required=True, help="Project name containing the task")
    parser_comp.add_argument("--task", required=True, help="Title of the task to close")
    parser_comp.set_defaults(func=handle_complete_task)

    # Command: list-projects
    parser_l_proj = subparsers.add_parser("list-projects", help="Review layout of all active projects")
    parser_l_proj.set_defaults(func=handle_list_projects)

    # Parse and execute context command
    args = parser.parse_args()
    args.func(args, users, projects)

if __name__ == "__main__":
    main()