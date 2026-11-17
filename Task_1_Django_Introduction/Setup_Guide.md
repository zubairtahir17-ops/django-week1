# Task 1 – Django Introduction

## Installation and Environment Setup

### 1. Check Python Installation

```powershell
python --version
```

### 2. Create Project Directory

```powershell
mkdir D:\Jamwah_Django_Internship\Task_1_Django_Introduction
cd D:\Jamwah_Django_Internship\Task_1_Django_Introduction
```

### 3. Create Virtual Environment

```powershell
python -m venv venv
```

### 4. Activate Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Verify pip

```powershell
python -m pip --version
```

### 6. Install Django

```powershell
python -m pip install django
```

### 7. Verify Django Installation

```powershell
python -m django --version
```

### 8. Create Django Project

```powershell
django-admin startproject intro_project .
```

### 9. Apply Database Migrations

```powershell
python manage.py migrate
```

### 10. Start Django Development Server

```powershell
python manage.py runserver
```

### 11. Open Website

http://127.0.0.1:8000/

### 12. Stop Development Server

Press CTRL + C in the terminal.

---

## Technologies Used

- Python 3.13
- Django 6.1.3
- pip 26.2.1
- Visual Studio Code
- PowerShell
- SQLite Database
- Python Virtual Environment

## Result

Successfully installed Django, configured a virtual environment, created a Django project, applied database migrations, and launched the development server. The default Django welcome page was displayed successfully.
