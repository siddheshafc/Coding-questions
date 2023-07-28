def find_missing_num(nums):
    n = len(nums) + 1
    expected_sum = (n * (n + 1) // 2)
    actual_sum = sum(nums)
    missing_num = expected_sum - actual_sum
    return missing_num

nums = [1,2,3,5,6,7,8]
print("The missing number in an array is: ", find_missing_num(nums))