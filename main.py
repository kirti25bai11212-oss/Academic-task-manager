import json
import os
import hashlib
import datetime
from datetime import datetime as dt

# --- CONFIGURATION ---
DATA_FILE = "app_data.json"

# --- DATA LAYER (Non-Functional Req: Reliability/Persistence) ---
class DataManager:
    """Handles loading and saving data to JSON."""

    @staticmethod
    def load_data():
        if not os.path.exists(DATA_FILE):
            # Initialize with empty structure if file doesn't exist
            return {"users": [], "tasks": []}
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {"users": [], "tasks": []}

    @staticmethod
    def save_data(data):
        try:
            with open(DATA_FILE, "w") as f:
                json.dump(data, f, indent=4)
        except IOError:
            print("Error saving data.")


# --- SECURITY MODULE (Non-Functional Req: Security) ---
class SecurityService:
    """Handles password hashing."""

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(stored_hash, provided_password):
        return stored_hash == hashlib.sha256(provided_password.encode()).hexdigest()


# --- MODULE 1: USER MANAGEMENT (Functional Req 1) ---
class UserManager:
    def _init_(self, data):
        self.data = data
        self.current_user = None

    def register(self):
        print("\n--- Register ---")
        username = input("Enter username: ").strip()
        if any(u["username"] == username for u in self.data["users"]):
            print("Username already exists.")
            return False

        password = input("Enter password: ").strip()
        if len(password) < 4:
            print("Password too short (min 4 chars).")
            return False

        hashed_pw = SecurityService.hash_password(password)
        new_user = {
            "id": len(self.data["users"]) + 1,
            "username": username,
            "password": hashed_pw,
            "joined_at": str(dt.now()),
        }
        self.data["users"].append(new_user)
        DataManager.save_data(self.data)
        print("Registration successful! Please login.")
        return True

    def login(self):
        print("\n--- Login ---")
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        user = next((u for u in self.data["users"] if u["username"] == username), None)

        if user and SecurityService.verify_password(user["password"], password):
            self.current_user = user
            print(f"Welcome, {username}!")
            return True
        else:
            print("Invalid credentials.")
            return False

    def logout(self):
        if self.current_user:
            self.current_user = None


# --- MODULE 2: TASK MANAGEMENT (Functional Req 2: CRUD) ---
class TaskManager:
    def _init_(self, data, user_manager):
        self.data = data
        self.user_manager = user_manager

    def create_task(self):
        print("\n--- Create Task ---")
        title = input("Task Title: ").strip()
        desc = input("Description: ").strip()
        priority = input("Priority (High/Medium/Low): ").strip().capitalize()

        # Input Validation
        if priority not in ["High", "Medium", "Low"]:
            print("Invalid priority. Defaulting to Medium.")
            priority = "Medium"

        new_task = {
            "id": len(self.data["tasks"]) + 1,
            "user_id": self.user_manager.current_user["id"],
            "title": title,
            "description": desc,
            "priority": priority,
            "status": "Pending",
            "created_at": str(dt.now().date()),
        }
        self.data["tasks"].append(new_task)
        DataManager.save_data(self.data)
        print("Task added successfully.")

    def view_tasks(self):
        print("\n--- Your Tasks ---")
        user_id = self.user_manager.current_user["id"]
        tasks = [t for t in self.data["tasks"] if t["user_id"] == user_id]

        if not tasks:
            print("No tasks found.")
            return

        print(f"{'ID':<5} {'Title':<20} {'Priority':<10} {'Status':<10}")
        print("-" * 50)
        for t in tasks:
            print(
                f"{t['id']:<5} {t['title']:<20} {t['priority']:<10} {t['status']:<10}"
            )

    def update_task_status(self):
        self.view_tasks()
        try:
            task_id = int(input("\nEnter Task ID to update: "))
            user_id = self.user_manager.current_user["id"]

            task = next(
                (
                    t
                    for t in self.data["tasks"]
                    if t["id"] == task_id and t["user_id"] == user_id
                ),
                None,
            )

            if task:
                new_status = input(
                    "Enter new status (Pending/In-Progress/Completed): "
                ).strip()
                task["status"] = new_status
                DataManager.save_data(self.data)
                print("Task updated.")
            else:
                print("Task not found or access denied.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def delete_task(self):
        self.view_tasks()
        try:
            task_id = int(input("\nEnter Task ID to delete: "))
            user_id = self.user_manager.current_user["id"]

            # Filter out the task to delete
            initial_count = len(self.data["tasks"])
            self.data["tasks"] = [
                t
                for t in self.data["tasks"]
                if not (t["id"] == task_id and t["user_id"] == user_id)
            ]

            if len(self.data["tasks"]) < initial_count:
                DataManager.save_data(self.data)
                print("Task deleted.")
            else:
                print("Task not found.")
        except ValueError:
            print("Invalid input.")


# --- MODULE 3: ANALYTICS (Functional Req 3: Reporting) ---
class AnalyticsEngine:
    def _init_(self, data, user_manager):
        self.data = data
        self.user_manager = user_manager

    def show_report(self):
        print("\n--- Productivity Report ---")
        user_id = self.user_manager.current_user["id"]
        tasks = [t for t in self.data["tasks"] if t["user_id"] == user_id]

        total = len(tasks)
        if total == 0:
            print("No data available for reporting.")
            return

        completed = sum(1 for t in tasks if t["status"] == "Completed")
        pending = sum(1 for t in tasks if t["status"] == "Pending")

        completion_rate = (completed / total) * 100

        print(f"Total Tasks: {total}")
        print(f"Completed:   {completed}")
        print(f"Pending:     {pending}")
        print(f"Efficiency:  {completion_rate:.2f}%")


# --- MAIN APPLICATION CONTROLLER (Workflow) ---
class Application:
    def _init_(self):
        self.data = DataManager.load_data()
        self.user_mgr = UserManager(self.data)
        self.task_mgr = TaskManager(self.data, self.user_mgr)
        self.analytics = AnalyticsEngine(self.data, self.user_mgr)

    def main_menu(self):
        while True:
            print("\n--- Academic Task Manager ---")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Select: ")

            if choice == "1":
                self.user_mgr.register()
            elif choice == "2":
                if self.user_mgr.login():
                    self.user_dashboard()
            elif choice == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid choice.")

    def user_dashboard(self):
        while True:
            print(f"\n--- Dashboard ({self.user_mgr.current_user['username']}) ---")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Update Task Status")
            print("4. Delete Task")
            print("5. View Analytics Report")
            print("6. Logout")
            choice = input("Select: ")

            if choice == "1":
                self.task_mgr.create_task()
            elif choice == "2":
                self.task_mgr.view_tasks()
            elif choice == "3":
                self.task_mgr.update_task_status()
            elif choice == "4":
                self.task_mgr.delete_task()
            elif choice == "5":
                self.analytics.show_report()
            elif choice == "6":
                self.user_mgr.logout()
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = Application()
    app.main_menu()
