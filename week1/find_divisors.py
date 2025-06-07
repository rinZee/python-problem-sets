'''
Problem 9: Divisors
Write a function find_divisors() that takes in an integer n as a parameter that returns a list of all divisors of n.

def find_divisors(n):
    pass
Example Usage:

lst = find_divisors(6)
print(lst)
Example Output:

[1, 2, 3, 6]

'''

def find_divisors(n):

    result = []
    for i in range(1, n+1):
        if n%i == 0:
            result.append(i)

    print(result)

find_divisors(6)
