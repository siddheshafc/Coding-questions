def pyramid(rows):
    for i in range(rows):
        for j in range(rows - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        print()

rows = int(input("Enter number of rows to be printed: "))
pyramid(rows)                