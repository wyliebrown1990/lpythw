#"import" This is how you add features to your script from the Python feature set.
from sys import argv
#The argv is the "argument variable," a very standard name in programming that you will find used in many other languages. This variable holds the arguments you pass to your Python script when you run it.
script, first, second, third = argv
#Line 3 "unpacks" argv so that, rather than holding all the arguments, it gets assigned to four variables you can work with: script, first, second, and third. This may look strange, but "unpack" is probably the best word to describe what it does. It just says, "Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order."

#Per the lesson, adding an input to this code
fourth = input("Enter your fourth variable: ")

#show the results
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)

#Here is what my CLI looks like: 
#(base) wyliebrown@Wylies-MBP-2 lpythw % python ex13.py first second third
#Enter your fourth variable: fourth
#The script is called: ex13.py
#Your first variable is: first
#Your second variable is: second
#Your third variable is: third
#Your fourth variable is: fourth
#(base) wyliebrown@Wylies-MBP-2 lpythw % 