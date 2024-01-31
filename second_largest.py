def find_second_largest(numbers):
    largest = float('-inf')
    second_largest = float('-inf')
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest


nums = [10, 5, 8, 20, 3]
second_largest_num = find_second_largest(nums)
print(f"Listedeki en büyük ikinci sayı:  {second_largest_num}")