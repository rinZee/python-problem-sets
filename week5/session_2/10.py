Problem 10: Print Backwards
Write a function print_reverse() that takes in the tail of a doubly linked list as a parameter.

It should print out the values of the linked list in reverse order, each separated by a space.

class Node:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev
		
def print_reverse(tail):
	pass
Example Usage: (using the doubly linked list from Problem 9)

#              (head)                       (tail)
# Linked List: Poliwag <-> Poliwhirl <-> Poliwrath
print_reverse(poliwrath)
Example Output: Poliwrath Poliwhirl Poliwag