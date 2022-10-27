class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self, data):
        self.head = Node(data)
    
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
    
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
    
    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            node = node.next
            cnt += 1
        
        return node.data

test = Linked_list(1)
test.append(2)
test.append(3)
test.append(4)

print()
test.print_all()