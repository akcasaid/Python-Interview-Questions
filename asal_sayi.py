def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test the function
num = 17
if is_prime(num):
    print(f"{num} sayısı bir asal sayıdır.")
else:
    print(f"{num} sayısı bir asal sayı değildir")