#Program to swap two numbers without using temporary variable

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Number before swapping are: {a} and {b}".format(a=num1, b=num2))
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("Numbers after swapping are: {a} and {b}".format(a=num1, b=num2))
