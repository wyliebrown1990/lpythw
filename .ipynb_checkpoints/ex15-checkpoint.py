#Lines 1-3 are using argv to get a filename
#First import the argv variable from the sys module
from sys import argv
#argv typically contains at least 2 elements with the first being the name of the script itself. This line unpacks the values contianed in the argv list into two variables: 'script' and 'filename'
script, filename = argv

#This is a new command for me that opens a file based on the filename element the user inputs in their first CLI command
txt = open(filename)

#This simply prints the name of the file next to a string
print(f"Here's your file {filename}:")
#We call a function on txt named read. What you get back from open is a file, and it also has commands you can give it. You give a file a command by using the . (dot or period), the name of the command, and parameters, just like with open and input. The difference is that txt.read() says, "Hey txt! Do your read command with no parameters!"
print(txt.read())

#This seems repetitive but it shows how to add a second prompt to dynamically open and read the file you input
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())