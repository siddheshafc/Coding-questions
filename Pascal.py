from math import factorial

n = int(input("Enter number of rows: "))

for i in range(n):
    for j in range(n - i + 1):
        print(end=" ")

    for j in range(i + 1):
        # Using nCr formula: n!/((n-r)!*r!)
        print(factorial(i) // (factorial(i-j) * factorial(j)), end=" ")
    print()

