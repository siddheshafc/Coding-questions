def rotate(arr, k):
    n = len(arr)
    rotate_arr = [0] * n

    for i in range(n):
        rotate_arr[(i + k) % n] = arr[i]
    return rotate_arr

array = [1,2,3,4,5]
rotation = 2
print("Original array: ", array)
print("Rotated Array: ", rotate(array,rotation))