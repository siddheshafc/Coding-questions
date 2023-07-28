num = int(input("Enter range: "))
a = 0
b = 1
nextTerm = 0

for i in range(num):
    print(nextTerm, end=" ")
    a = b
    b = nextTerm
    nextTerm = a + b
