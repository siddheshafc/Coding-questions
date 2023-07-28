str1 = input("Enter a string: ")

reversed_str = ""

for i in range(len(str1) - 1, -1, -1):
    reversed_str += str1[i]
    
print("the reversed string is:", reversed_str)


