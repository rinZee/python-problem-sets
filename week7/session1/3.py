#Problem 3: Recursive Sum
#Without using the built-in sum() function, write a function sum_list() that calculates the sum of all values in a list recursively.

#What is the time complexity of this function? What is the space complexity?

def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])
 
#Example Usage:
sum = sum_list([1, 2, 3, 4, 5])
print(sum)
# Example Input: [1, 2, 3, 4, 5]
#Example Output:

# Expected Output: 15
# Explanation: 1 + 2 + 3 + 4 + 5 = 15