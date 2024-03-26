# to run this in the terminal % python ex20.py ex20_test.txt


#The shorthand notation += is a compound assignment operator in Python. 
#It is used to add the value on the right-hand side to the variable on the left-hand side and then assign the result back to the variable.

#From the sys module import argv variable to allow for a list of arguments in your script
from sys import argv
#create a variable with a string for a name that is a txt file
input_file = "ex20_test.txt"

#create a function called print_all which is passed an argument of f. 
#When run, it will read and print the argument f
def print_all(f):
    print(f.read())

#create a function called rewind which is passed an argument of f. 
#When run, moves the file cursor (the marker that indicates the current position in the file) to the beginning of the file (position 0)
def rewind(f):
    f.seek(0)
#create a function called print_a_line that is passed 2 arguments. 
#When run, the readline method reads the next line from the file f. 
#The print function then prints the line_count followed by the line read from the file.
def print_a_line(line_count, f):
    print(line_count, f.readline())

#creates the variable current_file to open the input_file variable
current_file = open(input_file)

print("First let's print the whole file:\n")

#prints the entirety of the current file
print_all(current_file)
print("\n")
print("Now let's rewind. Kind of like a tape.\n")

#runs the rewind function, which moves the cursor to the beginning of the file
rewind(current_file)

print("Let's print 3 lines:\n")

#Initializes the variable current_line with value of 1
#calls the print_a_line functions with arguments current_line, current_file
current_line = 1
print_a_line(current_line, current_file)

#Increments the current_line cariable with 1 + 1 = 2
#calls the print_a_line functions with arguments current_line, current_file
current_line += 1
print_a_line(current_line, current_file)

#Increments the current_line cariable with 2 + 1 = 3
#calls the print_a_line functions with arguments current_line, current_file
current_line += 1
print_a_line(current_line, current_file)