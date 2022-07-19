# Overview

{Provide a description the software that you wrote and how it integrates with a Cloud Database.  Describe how to use your program.}
This is a console app to keep track of your pending tasks for the week. Select one option of the menu and create new tasks, display the list of tasks, edit a whole task, delete tasks, and delete one field of a task.  

This program will help anyone to follow up your most important tasks of the week.

[Software Demo Video will come soon](#)

# Cloud Database

Firebase - Cloud Firestore

The database is working with 5 principal fields: 
* Title of taks: String type
* Description of the task: String type
* Due time of the taks: String type (to be improved with data validation)
* Label of the task (optional): String type

# Development Environment

{Describe the tools that you used to develop the software}
* Python 3
* Firebase - Google Cloud Platform
* VScode

Python language.
firebase-admin package.

# Useful Websites

* [Get started with Firebase](https://firebase.google.com/docs/firestore/quickstart)
* [Python code examples](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/e9063143db274e1c4f6e12cf030c85e53dbf9592/firestore/cloud-client/snippets.py)

# Future Work

* Tkinter interface
* Improvement of CRUD logic for the database 