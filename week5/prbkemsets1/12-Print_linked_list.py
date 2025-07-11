#Problem 12: Printing Linked List
#Write a function print_linked_list() that takes in a head node as a parameter and prints the linked list using the string " -> " to separate each node.
#
#Note: The "head" of a linked list is the first element in the linked list, equivalent to lst[0] of a normal list.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next= next
  
        
		
def print_linked_list(head):
	current = head
	while current:
		if current.next:
			print(current.value, end=" -> ")
		else:
			print(current.value)
		current = current.next
#Example Input:

# input linked list: a->b->c->d->e
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")

a.next = b
b.next = c
c.next = d
d.next = e

print_linked_list(a)
#Example Output:

#a -> b -> c -> d -> e