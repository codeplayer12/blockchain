"""
Docstring for Getting Started.intro
Arg:
    usename: Get input from user and store in username
    file_name: Text file to store the username  and have access to read the file
"""
# file name to save the username in
file_name = "name.txt"

# Function to read user input and save the name to a file
def username():
    name = input("Please enter your name: ")
    file_write = open(file_name,mode='w')
    file_write.write(name)

# Calling the username function
username()
# Read the username in the file
file_read = open(file_name,mode='r')
# print the name in the filename
print(file_read.read())