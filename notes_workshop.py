# Python Regex Lesson

# Regular Expressions (regex) are a powerful tool for string pattern matching and manipulation. 
# In Python, the "re" module provides function to work with regular expressions.

# Basic Syntax: Some common metacharacters & special characters we use in regular expressions:
'''
    ***** META CHARACTERS *****
    ".": Any character except a newline
    "^": Start of a string
    "$": End of a string
    "*": Zero or more occurrences of the previous character
    "+": One or more occurrences of the previous character
    "?": Zero or one occurrence of the previous character
    "[]": Set of characters
    "|": Either/or condition
    "{}: Specify the exact number of occurences of the preceding character
    "\": Escape special characters (or use a "r" string)
    
    ***** SPECIAL CHARACTERS *****
    "\d": Matches any digit (0-9)
    "\D": Matches non-digit
    "\w": Matches any word characters (a-z, A-Z, 0-9, _)
    "\W: Matches any non-word character
    "\s": Matches any whitespace character (spaces, tabs, newlines)
    "\S": Matches any non-whitespace character
'''

import re
# 1. Common Functions & Methods with Regex


# re.search(): Searches for a pattern and returns the first occurrence
#NOTE: Always use "r" or "raw" strings when creating a pattern with regex
result = re.search(r'\d+', 'The house number is 1234')
print(result.group())

# re.findall(): Returns all matches in the string
results = re.findall(r'\d+', 'The Kinda Ka Rollercoaster is 456ft high and reaches up to 128mph')
print(results)


# re.sub(): Replaces a pattern with a new string
text = re.sub(r'michael jordan', 'kobe bryant', 'the goat will always be michael jordan')
print(text)


# re.split(): Splits the string by the occurrences of the pattern
parts = re.split(r'\s+', 'The Seahawks will win the superbowl.')
print(parts)





# 2. Grouping and Capturing: You can use parentheses (), to group parts of a regex pattern and capture a match 123-45-6789
ssn_pattern = r'(\d{3})-(\d{2})-(\d{4})'
result = re.search(ssn_pattern, 'My SSN is 123-45-6789')
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(3))


# Create a pattern for a full name with naming/capturing groups ("Christian Sachs")
full_name_pattern = r'(?P<first_name>[A-Z][a-z]+) (?P<last_name>[A-Z][a-z]+)'
result = re.search(full_name_pattern, 'My name is Christian Sachs')
print(result.group())
print(result.group('first_name'))
print(result.group('last_name'))




# 3. In-Class exercise
# Matching a Valid Email Address
email_string = 'my email for coding temple is: csachs@ct.com'
email_pattern = r'[a-z]+@\D+.\D+'
result = re.search(email_pattern, email_string)
print(result)