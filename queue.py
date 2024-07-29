# QUEUE 구현
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class queue:
    def __init__(self):
        self.front = None

    def push(self, value):
        if not self.front:
            self.front = Node(value, None)

    node = self.front
    while node.next:
        node = node.next
    node.next = Node(value, None)

    def pop(self):
        if not self.front:
            return None
        
        node = self.front
        self.front = self.front.next
        return node.item