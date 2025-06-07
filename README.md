# DevTrack – Developer Task & Time Tracker API

A backend API system designed to help individual developers or small teams manage tasks, track time, and generate reports on work activity. This project combines authentication, time-tracking logic, relational data models, and role-based access, making it ideal for intermediate developers building production-ready skills.

---

## 🚀 Features

🧩 Key Features:
### 1. User Authentication & Authorization
* **JWT Authentication** with token generation and refresh logic
* **Password hashing** using **Passlib**
* **Role-based access control (RBAC)**: admin, developer, viewer

### 2. Project & Task Management
* **CRUD operations** for Tasks
* **Tasks** have:
  * Title, description
  * Status (To Do, In Progress, Done)
  * Priority (Low, Medium, High)


### 3. Time Tracking Logic
* API endpoints to:
  * start, pause, resume, and stop a task timer
* Calculate total time spent per task automatically (in seconds)

### 4. Reporting
* Export data in **CSV/JSON**

---

# 🏗️ Tech Stack:
| **Component** |        **Tool/Library**         |
|:-:|:-------------------------------:|
| Web Framework |             FastAPI             |
| ORM |    SQLAlchemy (with Alembic)    |
| Data Validation |            Pydantic             |
| Auth | JWT (via python-jose) + Passlib |
| DB |           PostgreSQL            |
| Containerization |     Docker + Docker Compose     |

---

## 🧪 Sample API Endpoints

```http
/task/add_task
/task/start_task
/task/pause_task
/task/resume_task
/task/end_task
/user/signup
/user/update_user_role
```