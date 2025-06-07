'''
Problem 5: Max Difference
Write a function max_difference() that takes in a list of integers lst and returns the difference between the smallest and largest value in the list.

def max_difference(lst):
    pass
Example Usage:

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)
Example Output: 20

'''
def max_difference(lst):
    max=lst[0]
    min=lst[0]

    for i in lst:
        if i > max:
            max = i
        if i < min:
            min = i
        
    diff = max - min
    print(diff)

max_difference([5,22,8,10,2])
        
