'''
This is a note for Module 3 of Python Intermediate. 
This is a Multi-line String comment. 

Lesson :4 Python Regular Expressions

# There are four collection data types in the Python programming language: List, Tuple, Set, and Dictionary.

https://www.w3schools.com/python/python_regex.asp

https://docs.python.org/3/library/re.html#

'''

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# Python has a built-in package called re, which can be used to work with Regular Expressions.

import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(txt)
print(x)