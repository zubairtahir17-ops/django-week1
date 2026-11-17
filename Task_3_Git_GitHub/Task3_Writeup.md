# Task 3: Git & GitHub

## Objective

To learn Git version control, configure Git, initialize a repository, track project files, create commits, and upload the project to GitHub.

## 1. Git Installation Verification

Command:
`git --version`

Purpose:
Checks whether Git is installed and accessible through the terminal.

## 2. Git Configuration

Commands:

`git config --global user.name "Zubair Tahir"`

`git config --global user.email "m.zubairtahir17@gmail.com"`

Purpose:
Configures the username and email used to identify commits.

Verification:

`git config --global --list`

## 3. Repository Initialization

Command:

`git init`

Purpose:
Initializes a Git repository in the current project directory.

## 4. Checking Repository Status

Command:

`git status`

Purpose:
Displays tracked, untracked, and modified files.

## 5. Creating a README

Command:

`New-Item README.md -ItemType File`

Purpose:
Creates a README file to describe the project.

## 6. Staging Files

Commands:

`git add README.md`

`git add Task_1_Django_Introduction`

`git add Task_2_Python_Recap`

Purpose:
Stages selected files and folders for committing.

## 7. Creating Commits

Commands:

`git commit -m "Add internship README"`

`git commit -m "Add Django introduction task"`

`git commit -m "Add Python recap task"`

Purpose:
Creates snapshots of the staged changes.

## 8. Branch Management

Command:

`git branch -M main`

Purpose:
Renames the current branch to main.

## 9. Connecting GitHub Repository

Command:

`git remote add origin https://github.com/YOUR_USERNAME/django-week1.git`

Purpose:
Connects the local repository to the remote GitHub repository.

## 10. Uploading Project

Command:

`git push -u origin main`

Purpose:
Uploads local commits to GitHub and establishes upstream tracking.

## 11. Verifying Commit History

Command:

`git log --oneline`

Purpose:
Displays the repository's commit history in a compact format.

## 12. Final Verification

Command:

`git status`

Purpose:
Checks whether all changes have been committed and pushed.

## Outcome

Successfully installed and configured Git, initialized a local repository, tracked project files, created meaningful commits, connected the repository to GitHub, and uploaded the internship work.
