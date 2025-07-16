#Problem 5: Binary Search I
#Binary search is a searching algorithm that allows us to efficiently find the index of a given value within a sorted list. 
# Given the pseudo code for binary search below, implement an iterative (non-recursive) implementation of binary search. 
# There is also a recursive alternative that we’ll cover in the session 2 problem set!

#Evaluate the time and space complexity of your implementation.

def binary_search(lst, target):
	# Initialize a left pointer to the 0th index in the list
    left = 0
	# Initialize a right pointer to the last index in the list
    right = len(lst) - 1
    
    while left <= right:
        middle = (left + right) // 2
        if lst[middle] == target:
            return middle
        elif lst[middle]< target:
            left = middle + 1
        else:
            right = middle -1
	
	# If we search whole list and haven't found target value, return -1
    return -1

#def binary_search(lst, target):
#	pass

#Example Usage:

print(binary_search([1, 3, 5, 7, 9, 11, 13, 15],11))
#Example Output:

# Expected Output: 5
# Explanation: 11 has index 5 in the list