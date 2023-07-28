def is_pangram(string):
    alphabets = "abcdefghijklmnopqrstuwxyz"
    string = string.lower()
    for char in alphabets:
        if char not in string:
            return False
        else:
            return True

string = input("Enter a string: ")
if is_pangram(string):
    print("The given string is an Pangram")
else:
    print("The given string is not an Pangram")
