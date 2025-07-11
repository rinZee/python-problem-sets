#Problem 10: Linking Nodes
#Building off the Node class from Problem 9, now we will link the nodes together.

#To link the nodes, we can set a node's next attribute to hold another node. Update node_one from the Problem 9 to point to node_two.
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

node_two = Node('b')
node_one = Node('a', node_two)

print(node_one.value)
print(node_one.next.value)
print(node_two.value)

#Example Output:

#a
#b
#b