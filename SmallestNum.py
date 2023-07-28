def find_smallest(arr):
    if len(arr) == 0:
        return None
    
    smallest = arr[0]
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest

arr = [5,7,5,1,4,3,2,9,6]

print("The smallest number in an array is: ", find_smallest(arr))