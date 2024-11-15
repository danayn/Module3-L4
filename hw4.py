#Assignments: Python Regex
'''
1. Python Regular Expressions Deep Dive

Objective: The aim of this assignment is to deepen your practical skills in Python's regular expressions, 
enhancing your ability to process and manipulate text data. You will tackle a variety of real-world scenarios, 
applying regex to extract, validate, and transform text effectively.

Task 1: Email Extraction Enhancement

Problem Statement: You have a script that extracts email addresses from a text but needs to be refined to 
exclude certain domains (e.g., '[exclude.com](http://exclude.com/)'). Modify the script to extract all email addresses
 except those from the specified domain.

Code Example:

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)
Adapt the regex pattern to exclude email addresses from '[exclude.com](http://exclude.com/)'.

Ensure the script still extracts all other valid email addresses. 
NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and 
clicks the run button at the top, all code executes as intended. For example, if there are if statements, 
print statements, or for loops, they should function correctly and display output in the console as expected. 
If you have a function, make sure the function is called and runs.

The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.
+[^exclude.com]
'''

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
emailse = []
for item in emails:
    if "exclude.com" not in item:
         emailse.append(item)

print(emails)
print("The solution with extraction is below: ")
print(emailse)

