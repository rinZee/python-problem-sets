'''
def cast_vote(votes, candidate):

# crete an empty dictionary
    if candidate in votes:
        votes[candidate] = votes[candidate] + 1
    else:
        votes[candidate] = 1
    return votes



# loop through the keys in the dictonary
    ##for vote in votes.keys():
    # check if the keu already exists, increment the value by 1
       ## print(votes[vote])
    # else it doesnt, create a new key and assign the value 1
# return the new dictionary


votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)

cast_vote(votes, "Gina")
print(votes)
'''

'''
#1 create an empty list
#2 create a loop for dict 1 and check if the keys are similar to dict 2
    #append to the new list
#3 return the new list

def common_keys(dict1, dict2):
    empty_list = []
    for i in dict1:
        if i in dict2:
            empty_list.append(i)
    return empty_list


dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)
'''

#1find the highest priority task
#2 remove it from the dictionary and print it
#3 print the dictionary

def perform_task():
    

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)
