def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

nums = [10, 5, 8, 20, 3]
largest_num = find_largest(nums)
print(f"En büyük sayı:  {largest_num}")