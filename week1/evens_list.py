'''
Problem 7: Evens List
Write a function get_evens() that takes in a list of integers lst as a parameter and returns a list of all even numbers in the list.

def get_evens(lst):
    pass
Example Usage:

lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)
Example Output:

[2, 4]

'''
def get_evens(lst):
    evens_list = []
    for i in lst:
        if i%2 == 0:
            evens_list.append(i)

    print(evens_list)

get_evens([1,2,3,4])