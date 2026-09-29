# Campus-lost-And-found-
1. Project Title
Campus Lost and Found System

2. Overview of the Project
Campus Lost and Found is a Python-based console application designed to help students manage lost and found items on a campus.
The system allows users to register, report lost items, report found items, search for items, find possible matches between lost and found records, claim found items, and view basic reports and statistics.
The project uses SQLite to store the data locally, so no separate database server is required.

3. Features
User Registration
Allows a user to register with their name and email.
Checks that required fields are not empty.
Performs basic email validation.
Prevents duplicate email addresses.
Report Lost Item
Records the item name.
Stores a description of the item.
Stores the location where it was lost.
Stores the date of the incident.
Saves the record in the SQLite database.
Report Found Item
Records the item name.
Stores a description of the item.
Stores the location where it was found.
Stores the date of the incident.
Saves the record in the SQLite database.
Search Items
Searches both lost and found records.
Search can be performed using the item name, description, or location.
Possible Match Detection
Compares a lost item with available found items.
Calculates a similarity score based on:
Item name
Description
Location
Displays match levels such as Weak Match, Possible Match, Strong Match, and Very Strong Match.
Claim Found Item
Allows a found item to be marked as CLAIMED.
Prevents an already claimed item from being claimed again.
Reports and Statistics
The application displays:
Total lost items
Total found items
Total claimed items
Total unclaimed items

4. Technologies / Tools Used

Python 3
SQLite3 – local database management
VS Code or any Python-compatible IDE
Git and GitHub – source-code management and project submission
Python Modules Used
sqlite3 – database operations
Python functions and control structures – application logic
No external Python package is required for the current version.

5. Project Structure

Campus-Lost-and-Found/
│
├── main.py
├── database.py
├── matcher.py
├── users.py
├── lost_found.db
└── README.md

File Description
File
Purpose
main.py
Main menu and application workflow
database.py
Creates and updates the SQLite database tables
matcher.py
Calculates similarity between lost and found items
users.py
Creates the users table and handles user registration
lost_found.db
SQLite database containing project data
README.md
Project documentation

6. Database Design
The project uses SQLite and stores its data in lost_found.db.
Lost Items Table
Stores:
Item ID
Item name
Description
Location
Date
Status
The default status for a lost item is LOST.
Found Items Table
Stores:
Item ID
Item name
Description
Location
Date
Status
The default status for a found item is FOUND.
Users Table
Stores:
User ID
Name
Email
Email addresses are unique, so the same email cannot be registered twice.

7. Steps to Install & Run the Project

Step 1: Install Python
Install Python 3 on your computer.
Check whether Python is installed:
python --version
If the command does not work, try:
py --version

Step 2: Download or Clone the Repository
After uploading this project to GitHub, clone it using:
git clone YOUR_GITHUB_REPOSITORY_LINK
Then open the project folder.

Step 3: Open the Project in VS Code
Open the project folder in VS Code.
Make sure all the following files are in the same folder:
main.py
database.py
matcher.py
users.py
lost_found.db

Step 4: Run the Application
Open the VS Code terminal and run:
python main.py
If your system uses the py command, use:
py main.py

8. Instructions for Testing
After starting the program, the main menu will appear.
===================================
      CAMPUS LOST AND FOUND
===================================
1. Register User
2. Report Lost Item
3. Report Found Item
4. Search Items
5. Find Possible Matches
6. Claim Found Item
7. Reports
8. Exit

Test 1: Register a User

Select option 1.

Enter a name.
Enter a valid email address.
Confirm that the registration message appears.
Try the same email again to check duplicate-email handling.

Test 2: Report a Lost Item

Select option 2.
Enter the item name.
Enter its description.
Enter the location.
Enter the date.
Confirm that the item is recorded successfully.

Test 3: Report a Found Item

Select option 3.
Enter the item name.
Enter its description.
Enter the location.
Enter the date.
Confirm that the found item is saved.

Test 4: Search Items

Select option 4.
Enter a keyword related to an item.
Check the displayed lost and found results.

Test 5: Find Possible Matches

First create at least one lost item and one found item.

Select option 5.

Enter the ID of the lost item.
Check the calculated match score and match level.

Test 6: Claim a Found Item

Select option 6.
Enter the ID of a found item.
Confirm that its status changes to CLAIMED.
Try claiming the same item again and verify that the program reports that it has already been claimed.

Test 7: Reports

Select option 7.
Check the total number of lost items.
Check the total number of found items.
Check claimed and unclaimed item counts.

Test 8: Exit

Select option 8 to close the application.

9. Matching Logic

The matching system compares a lost item with found items and generates a score.
Exact item-name match: +40 points
Partial item-name match: +25 points
Three or more common description words: +30 points
One or more common description words: +15 points
Exact location match: +30 points
Partial location match: +15 points
Only matches with a score of 30 or higher are displayed.
The application categorizes displayed matches as:
80% or higher: Very Strong Match
60%–79%: Strong Match
40%–59%: Possible Match
Below 40%: Weak Match

10. Screenshots

Screenshots can be added here to demonstrate the working application.
Recommended screenshots:
Main menu
User registration
Lost item reporting
Found item reporting
Search results
Possible match results
Claiming an item
Reports and statistics
Example:

screenshots:- 
<img width="1390" height="926" alt="1" src="https://github.com/user-attachments/assets/16efd5e2-044d-43b9-b906-611fc6a519b0" />
<img width="1403" height="927" alt="image" src="https://github.com/user-attachments/assets/c94943c2-24ee-45e5-aa65-042eb5a7c7dc" />
<img width="1382" height="925" alt="image" src="https://github.com/user-attachments/assets/15a9b4b7-76d0-402c-93e7-f2454324b147" />
<img width="1397" height="927" alt="image" src="https://github.com/user-attachments/assets/376b5368-a4b6-49a0-a47f-1ae3c5bb0fc7" />
<img width="1383" height="917" alt="image" src="https://github.com/user-attachments/assets/2e6e2806-beb9-45ad-ad4c-a110e24fa1de" />
<img width="1408" height="923" alt="image" src="https://github.com/user-attachments/assets/52c37698-a255-4c02-9038-5ecc99506a52" />
<img width="1393" height="920" alt="image" src="https://github.com/user-attachments/assets/37b38272-c516-4190-999e-d25c54ed46ad" />
<img width="1413" height="928" alt="image" src="https://github.com/user-attachments/assets/1d9cdd61-1fae-4e44-9b8c-f4980201f8a0" />
<img width="1406" height="745" alt="image" src="https://github.com/user-attachments/assets/4d49e64e-dd6d-4120-9c4c-fc086bd31c5d" />

11. Expected Result
The program should successfully provide a simple campus-based system for recording and searching lost and found items.
Users should be able to enter item information, search existing records, identify possible matches, mark found items as claimed, and view basic statistics.

12. Future Improvements
Possible future improvements include:
Login and logout functionality
Separate accounts for users
User-specific item management
Password protection
Better matching using advanced text similarity
Graphical user interface
Image upload for lost and found items
Automatic date and time
Admin dashboard
Email notifications
Web-based version
Email notifications

Web-based version
