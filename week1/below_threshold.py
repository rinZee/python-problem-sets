'''
Problem 6: Below Threshold
Write a function count_less_than() that takes in a list of integers numbers and an integer threshold as parameters and returns the number of items in numbers that are less than threshold.

def count_less_than(numbers, threshold):
    pass
Example Usage:

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)
Example Output: 3

'''
def count_less_than(numbers, threshold):
    new_list = []
    result = 0
    for i in numbers:
        if i < threshold:
            new_list.append(i)
            result += 1
    
    print(new_list)
    print(result)

count_less_than([12,8,2,4,4,10], 5)