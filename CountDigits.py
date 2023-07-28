num = int((input("Enter a number: ")))  

count = 0 
while num != 0:
    num //= 10
    count += 1
  
print("The count for the given number is: ", count)    