def is_substring(string, substring):
    if substring in string:
        return True
    else:
        return False
    
string = input("Enter a string: ") 
substring = input("Enter a substring: ")

if is_substring(string, substring):
    print("Substring found!")
else:
    print("Substring not found.")    