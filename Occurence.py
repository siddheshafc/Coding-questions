#Program to count occurrence of a given character in a string

def count_occurance(string, char):
    count = 0
    for i in range(len(string)):
        if string[i] == char:
            count += 1
    return count

string = input("Enter a string: ")
char = input("Enter a character: ")

print("The occurance of ",char," in string ",string, "is: ", count_occurance(string, char))