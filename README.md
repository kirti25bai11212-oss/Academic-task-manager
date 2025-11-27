# Academic-task-manager
The Academic Task Manager is a desktop-based Command Line Interface (CLI) application developed using Python. It is designed to assist students and professionals in organizing their daily academic and personal responsibilities. The system provides a centralized platform to create, track, and manage tasks with varying priority levels. 
# Academic Task Manager

> A secure, modular Command Line Interface (CLI) application for managing personal tasks, featuring user authentication, data persistence, and productivity analytics.


**Project Overview**
The *Academic Task Manager* is a Python-based productivity tool designed to help students and professionals organize their daily workload.

Unlike simple script-based to-do lists, this application utilizes a *Service-Oriented Architecture (SOA)* on a micro-scale. It separates concerns between data management, security, and business logic, making the code robust and scalable. It supports multiple users on a single machine by ensuring data isolation and secure password handling.

**Key Features**
*Secure Authentication:* Users can register and login safely. Passwords are hashed using *SHA-256* (via hashlib) before storage, ensuring no plain-text credentials exist.
* Data Persistence:* All users and tasks are automatically saved to a local app_data.json file. Data remains available even after restarting the application.
  * Comprehensive Task CRUD:*
    * Create: Add tasks with Titles, Descriptions, and Priority levels (High/Medium/Low).
    * Read: View a formatted dashboard of your specific tasks.
    * Update: Change task status (Pending $\rightarrow$ In-Progress $\rightarrow$ Completed).
    * Delete: Remove unwanted tasks permanently.
* Productivity Analytics: A built-in engine calculates your efficiency based on the ratio of completed vs. pending tasks.
  * Data Isolation: The system filters data by User ID, ensuring users cannot see or modify each other's tasks.

**Technologies Used**
* Language: Python 3.6+
* Core Libraries:
    * json: For database serialization/deserialization.
    * hashlib: For cryptographic password hashing.
    * os: For file system integrity checks.
    * datetime: For timestamps.

  Installation and Execution

   **Prerequisites**
* Python 3.x installed on your system.

**Setup Steps**
1.  Clone the Repository (or download the source files):
    bash
    git clone [https://github.com/your-username/academic-task-manager.git](https://github.com/your-username/academic-task-manager.git)
    cd academic-task-manager
    

2.  Verify File Structure:
    Ensure task_manager.py (or your main script name) is present.

3.  Run the Application:
    bash
    python task_manager.py
    

4.  First Run:
    The application will automatically initialize and create a app_data.json file in the root directory to serve as the database.

 **Instructions for Testing**
Since this is a CLI application, you can verify functionality by following this manual test script:

**1. User Registration (Security Test)**
* *Action:* Select Option 1 and register a new user.
* *Expected Result:* Success message.
* *Verification:* Open app_data.json and verify the password field contains a long hash string, not the actual password.

**2. Login & Dashboard (Session Test)**
* *Action:* Select Option 2 and login with your new credentials.
* *Expected Result:* You gain access to the dashboard, and the prompt displays your username.

**3. Task Management (CRUD Test)**
* *Action:* Add a new task (Option 1).
* *Action:* View tasks (Option 2).
* *Expected Result:* The new task appears in the table with "Pending" status.

**4. Analytics (Logic Test)**
* *Action:* Mark a task as "Completed" (Option 3).
* *Action:* View Analytics (Option 5).
* *Expected Result:* If you have 1 task and it is completed, the efficiency score should be *100.00%*.

![output](https://github.com/user-attachments/assets/ebb05824-255a-4f7b-b3b2-a312510dcdfe)
<img width="2172" height="9640" alt="code" src="https://github.com/user-attachments/assets/59bac3b9-81a9-4418-94d8-cb9af2601ceb" />
