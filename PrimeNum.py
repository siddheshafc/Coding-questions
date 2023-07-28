# prime number program

num = int(input("Enter a number: "))

flag = False

if (num == 1):
    print("1 is not a prime number")
elif num > 1:    
    for i in range(2, num):
        if (num % i == 0):
            flag = True
            break
        
    if flag:
        print("The number {0} is not a prime number".format(num))
    else:
        print("The number {0} is prime number".format(num))            

