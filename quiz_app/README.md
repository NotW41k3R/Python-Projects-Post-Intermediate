# Trivia Quiz App (Tkinter + Open Trivia DB)
Completed on Day 34 of 100 Days of Python

A GUI-based True/False trivia quiz application built using Python and Tkinter, powered by real-time questions fetched from the Open Trivia Database API. The app presents questions one at a time, lets the user answer via buttons, provides instant visual feedback, and tracks the score throughout the quiz.

The project follows a clean object-oriented design, separating concerns across data handling, quiz logic, question modeling, and user interface. Questions are fetched once from the API, converted into Question objects, and then managed locally to avoid unnecessary API calls and rate limits.

Skills learned: working with REST APIs and JSON data using requests, applying object-oriented programming to structure applications, managing quiz state and logic flow, building event-driven GUIs with Tkinter, handling timed UI feedback using after() .