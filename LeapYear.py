# to check whether the given year is a leap year or not

num = int(input("Enter year: "))

if (num % 400 == 0) or (num % 4 == 0 and num % 100 != 0):
    print("The year {0} is a leap year".format(num))
else:
    print("The year {0} is not a leap year".format(num))
        