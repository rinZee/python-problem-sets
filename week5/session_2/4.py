#Problem 4: Get Tail
#Write a function get_tail() that takes in the head of a linked list as a parameter.

#It should print out the value of the tail of the list.

#If the list is empty (head is None), return None.
#Note: The "tail" of a list is the last element in the linked list. Equivalent to lst[-1] in a normal list.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def get_tail(head):
	if head:
		while head.next:
			head = head.next
		return head.value	
	else:
		return None


num1 = Node('num1')
num2 = Node('num2')
num3 = Node('num3')

num1.next = num2
num2.next = num3


#Example Usage:

# linked list: num1->num2->num3
head = num1
tail = get_tail(num1)
print(tail)
#Example Output: num3