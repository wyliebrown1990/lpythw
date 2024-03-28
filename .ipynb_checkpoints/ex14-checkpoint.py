from sys import argv

script, user_name, galaxy = argv
prompt = '< '

print(f"Hi {user_name} of the {galaxy} galaxy, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you mac and cheese {user_name}?")
likes = input(prompt)

print(f"Where do you most frequently poop {user_name}?")
lives = input(prompt)

print("What kind of toilet do you have?")
computer = input(prompt)

print(f"""
Alright so you said {likes} about liking mac and cheese.
You poop in {lives}. Not sure where that is.
And you have a {computer} toilet. Nice.
""")