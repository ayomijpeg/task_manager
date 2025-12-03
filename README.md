# Task Management API (Capstone Project)

A RESTful API for managing tasks, built with Django and Django REST Framework. This API allows users to create, read, update, and delete tasks with priority levels and completion status.

**Live Demo:** [https://ayomi.pythonanywhere.com/api/tasks/](https://ayomi.pythonanywhere.com/api/tasks/)

## 🔑 Test Credentials
To evaluate the API, please use the following credentials or create a new user via the `/api/users/` endpoint.

* **Username:** reviewer
* **Password:** password123

## 🚀 Features
* **User Authentication:** Users can only manage their own tasks.
* **CRUD Operations:** Full management of tasks.
* **Filtering:** Filter tasks by status (`?status=Pending`) or priority (`?priority=High`).
* **Sorting:** Sort by due date (`?ordering=due_date`).

## 📚 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/users/` | Create a new user account |
| `GET` | `/api/tasks/` | List all tasks for logged-in user |
| `POST` | `/api/tasks/` | Create a new task |
| `GET` | `/api/tasks/<id>/` | View task details |
| `PUT` | `/api/tasks/<id>/` | Update a task |
| `DELETE` | `/api/tasks/<id>/` | Delete a task |
| `POST` | `/api/tasks/<id>/mark_complete/` | Mark task as completed |

## 🛠️ Tech Stack
* Python 3.10
* Django 5.x
* Django REST Framework
* Deployed on PythonAnywhere
