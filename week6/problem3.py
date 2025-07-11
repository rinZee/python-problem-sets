class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    @staticmethod
    def count_element(head, val):
        count = 0
        current = head

        while current:
            if current.value == val:
                count += 1
            current = current.next
        print(f"Count of {val}: {count}")
        return count

    def __str__(self):
        # Custom print for linked list
        result = []
        current = self
        while current:
            result.append(str(current.value))
            current = current.next
        return " -> ".join(result)


# Create linked list: 3 -> 1 -> 2 -> 1
head = Node(3, Node(1, Node(2, Node(1))))

# Print the list
print("Linked List:", head)

# Count occurrences of 1
Node.count_element(head, 1)
