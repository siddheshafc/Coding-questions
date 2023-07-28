#Program to find all pairs of elements in an integer array

arr = [4, 6, 8, 10, 12, 14, 16]

n = len(arr)
num = 18
for i in range(0, n):
    for j in range(i+1,n):
        if(arr[i]+arr[j] == num):
            print(arr[i], " + ", arr[j], "=", num)
            