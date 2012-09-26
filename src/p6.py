# coding=utf-8
"""
The sum of the squares of the first ten natural numbers is,
1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
"""

def square_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i*i
    return sum

def sum_square(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum*sum

def diff(n):
    return sum_square(n) - square_sum(n)

assert diff(10) == 2640
print diff(100)
