def remove_duplicates(arr):
    unique_elements = []
    for element in arr:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

array = [1,1,2,4,5,6,4,5,3,2,1,6]
print("Array without duplicates: ", remove_duplicates(array))        