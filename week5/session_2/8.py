Problem 8: Linked Listify
Write a function list_to_linked_list() that takes in a list lst as a parameter and converts it to a linked list. The function should return the head of the linked list.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def list_to_linked_list(lst):
	pass
Example Usage:

normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
linked_list = list_to_linked_list(normal_list)
print(linked_list) # Only prints the head element!
Example Output:

Betty # Linked list : Betty -> Veronica -> Archie -> Jughead