# Fibonacci serisi, her sayının kendisinden önceki iki sayının toplamı olduğu bir sayı dizisidir. 
# The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding numbers.

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonacci(10) 