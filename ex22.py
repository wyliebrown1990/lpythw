import sys
script, input_encoding, error = sys.argv

#create a function called main that handles 3 arguments. 
#the readline() method is used to read a single line from a file. It's part of the file object's methods and is particularly useful when you want to read a file line by line, instead of reading the entire file content into memory at once.
def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

#In Python, the strip() method is used to remove leading and trailing whitespace characters (such as spaces, tabs, and newline characters) from a string. It doesn't modify the original string but returns a new string with the whitespace removed.
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)