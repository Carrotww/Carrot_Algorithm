class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
        return

    def pop(self):
        if self.is_empty():
            return "stack is Empty"
        current_node = self.head
        self.head = self.head.next
        return current_node

    def peek(self):
        if self.is_empty():
            return "stack is Empty"

        return self.head.data

    def is_empty(self):
        return self.head is None

test = Stack()
test.push(4)
print(test.peek())
test.push(3)
print(test.peek())
test.pop()
test.pop()
print(test.is_empty())
