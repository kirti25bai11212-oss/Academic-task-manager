**Project Statement: Academic Task Manager**

**1. Problem Statement**
In academic and professional environments, individuals face an increasing volume of assignments, deadlines, and administrative duties. Without a centralized system to track these obligations, users frequently experience:
* Task Fragmentation: Losing track of to-do items scattered across notes, mental lists, and emails.
* Prioritization Issues: Inability to distinguish between high-priority deadlines and low-priority chores.
* Lack of Insight: No visibility into personal productivity trends or completion rates.

There is a need for a lightweight, distraction-free tool that allows users to capture, organize, and analyze their tasks without the complexity or connectivity requirements of heavy web-based project management software.

 **2. Scope of the Project**
The Academic Task Manager is a localized, command-line based application designed to solve the problems listed above through a modular architecture.


**3. Target Users**
The application is tailored for individuals who prefer keyboard-centric workflows and require offline accessibility:

* University Students: For managing assignment deadlines, study schedules, and extracurricular activities.
* Developers & Sysadmins: Users comfortable with terminal environments who prefer CLI tools over GUI applications.
* Freelancers: For tracking individual project tasks and gauging personal productivity efficiency.

 **4. High-Level Features**
The system is built upon four main functional pillars:

**A. Secure Access Control**
* Registration: Ability to create a new user profile with a unique username.
* Authentication: Secure login mechanism verifying hashed credentials.
* Session Handling: Isolation of user data so that User A cannot access User B's tasks.

 **B. Task Management (CRUD)**
* Create: functionality to input Task Title, Description, and Priority (High/Medium/Low).
* Read: View a formatted dashboard of pending and completed tasks.
* Update: Modify the status of existing tasks (e.g., moving from 'Pending' to 'Completed').
* Delete: Remove tasks that are no longer relevant.

**C. Data Persistence**
* Auto-Save: The system automatically writes to the local JSON database after every creation, update, or deletion event, ensuring no data is lost if the application closes.
