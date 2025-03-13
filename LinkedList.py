import random

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: int):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        print(elements)

if __name__ == '__main__':
    ll = LinkedList()

    ll.append(1)
    ll.append(23)
    ll.append(14)
    ll.append(5)
    ll.append(12)

    print("Verkettete Liste:")
    ll.display()

    print(f"Länge der Liste: {len(ll)}")
