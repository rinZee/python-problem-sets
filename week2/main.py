# Problem 1: Subsequence
'''def is_subsequence(lst, sequence):
    for num in lst:
        for i in sequence:
            if i not in lst:
                return(False)
    return(True)


lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 100]
print(is_subsequence(lst, sequence))

def create_dictionary(keys, values):
    dict = {}
    length = len(keys)
    for k in range(length):
        dict[keys[k]] = values[k]
        
    return dict

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys, values))
'''
'''
Problem 3: Print Pair
Write a function print_pair() that takes in a dictionary dictionary and a key target as parameters. The function looks for the target and when found, it prints the key and it's associated value as "Key: <key>" followed by "Value: <value>". If target is not in dictionary, print "That pair does not exist!".

def print_pair(dictionary, target):
    pass
Example Usage:

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")
Example Output:

Key: patrick
Value: star
That pair does not exist!
Key: spongebob
Value: squarepants
'''
'''def print_pair(dictionary, target):
    keys = dictionary.keys()
    
    for i in keys:
        for num in range(len(dictionary)):
        if dictionary[num] == i

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")
'''
'''
my_dict = {"Audrey" : 90, "mario": 95, "char": 60}

def get_top(dictionary):
    high_score = 0
    top_player = ''
    for name, score in dictionary.items():
        if score > high_score:
            high_score = score
            top_player = name
    return top_player

print(get_top(my_dict))

'''

