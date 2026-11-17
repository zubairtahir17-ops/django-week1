# Task 4: Virtual Environments & pip

## Objective

To understand Python virtual environments, manage packages using pip, generate requirements.txt, and recreate an environment using the saved dependencies.

## 1. Checking Python Version

Command:

`python --version`

Purpose:
Checks the installed Python version.

## 2. Checking pip

Command:

`python -m pip --version`

Purpose:
Checks the installed pip version and its location.

## 3. Creating a Virtual Environment

Command:

`python -m venv venv`

Purpose:
Creates an isolated Python environment named venv.

## 4. Activating Virtual Environment

Command:

`.\venv\Scripts\Activate.ps1`

Purpose:
Activates the virtual environment in Windows PowerShell.

## 5. Upgrading pip

Command:

`python -m pip install --upgrade pip`

Purpose:
Upgrades pip to the latest available version.

## 6. Installing Django

Command:

`python -m pip install django`

Purpose:
Installs Django and its required dependencies into the active environment.

## 7. Verifying Django

Command:

`python -m django --version`

Purpose:
Displays the installed Django version.

## 8. Listing Installed Packages

Command:

`python -m pip list`

Purpose:
Displays packages installed in the active environment.

## 9. Generating requirements.txt

Command:

`python -m pip freeze > requirements.txt`

Purpose:
Records installed packages and their exact versions in requirements.txt.

## 10. Deactivating Virtual Environment

Command:

`deactivate`

Purpose:
Exits the currently active virtual environment.

## 11. Recreating Virtual Environment

Command:

`python -m venv venv`

Purpose:
Creates a fresh virtual environment.

## 12. Installing Dependencies from requirements.txt

Command:

`python -m pip install -r requirements.txt`

Purpose:
Installs all dependencies listed in requirements.txt.

## 13. Git Ignore Configuration

File:

`.gitignore`

Purpose:
Prevents unnecessary files, virtual environments, Python cache files, and sensitive environment variables from being uploaded to GitHub.

## Outcome

Successfully created and managed a Python virtual environment, installed Django using pip, generated requirements.txt, and learned how to recreate the environment using saved dependencies.
