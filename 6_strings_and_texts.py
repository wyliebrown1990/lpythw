{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "43d355cf-e234-40cb-9ec4-938ca743ce95",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are 10 types of people.\n",
      "Those who binary and those who don't.\n",
      "I said: There are 10 types of people.\n",
      "I also said: 'Those who binary and those who don't.'\n",
      "Isn't that joke so funny?! False\n",
      "This is the left side of...a string with a right side.\n"
     ]
    }
   ],
   "source": [
    "#this line creates a variable with a number value assigned to it and then creates a second variable that creates a string with the first variable within it\n",
    "types_of_people = 10\n",
    "x = f\"There are {types_of_people} types of people.\"\n",
    "\n",
    "#this line creates 3 variables and in the third variable it creates a string with the first 2 variables within it\n",
    "binary = \"binary\"\n",
    "do_not = \"don't\"\n",
    "y = f\"Those who {binary} and those who {do_not}.\"\n",
    "\n",
    "#these lines print the 2 groups of variables above in such a way that all of the variables are being used\n",
    "print(x)\n",
    "print(y)\n",
    "\n",
    "#this line also combines previous variables into a print that results in the multi-variable x and y within a string. \n",
    "print(f\"I said: {x}\")\n",
    "print(f\"I also said: '{y}'\")\n",
    "\n",
    "#this line states that the variable hilarious is False\n",
    "hilarious = False\n",
    "#this line creates a varible which is a string with an empty space for a format\n",
    "joke_evaluation = \"Isn't that joke so funny?! {}\"\n",
    "\n",
    "#this line prints the joke_evaluation variable with a second variable immeidately after it\n",
    "print(joke_evaluation.format(hilarious))\n",
    "\n",
    "#these lines create 2 variables with strings that are later printed next to one another. the use of the + concatenates the two strings into 1 longer string\n",
    "w = \"This is the left side of...\"\n",
    "e = \"a string with a right side.\"\n",
    "print(w + e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "beb6177d-cb71-479c-9429-790d6bbca5fd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
