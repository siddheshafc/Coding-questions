num = int(input("Enter a number: "))
fac = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        fac = fac * i

print("Factorial of {a} is : {b}".format(a = num, b = fac))

