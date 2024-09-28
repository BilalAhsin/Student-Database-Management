Student Registration System
This project is a simple command-line application that allows users to register student names with unique IDs. It ensures that no duplicate names are entered and displays the registered names along with their IDs.

Features
Register student names until the user decides to stop.
Prevent duplicate names from being added.
Automatically assign a unique ID to each student.
Display a formatted list of registered students with their IDs.
Requirements
Python 3.x
Code Explanation
The program initializes two lists: students for storing student names and id for storing unique IDs.
A while loop is used to continuously prompt the user for student names.
If the user inputs a name that already exists in the students list, a message will inform them of the duplicate entry.
Upon entering a new name, it will be added to the list along with an automatically incremented ID.
After registration is complete, the program prints a formatted list of student IDs and names.