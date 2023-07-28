num = int(input("Enter a number: "))
rem = 0
sum = 0

while num != 0:
    rem = num % 10
    sum = sum + rem
    num //= 10

print("The sum of number is: ", sum)
    
