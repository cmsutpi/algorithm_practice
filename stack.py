#stack 구현

class Node:
    def __init__(self,item,next):
        self.item = item
        self.next = next

class stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self,value):
        self.top = Node(value, None)

    def pop(self):
        if self.top is None:
            return None
        
        node = self.top
        self.top = self.top.next
        
        return node.item