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
        
        return node
    
    def add_node(self, index, value):
        input_node = Node(value)
        if index == 0:
            input_node.next = self.head
            self.head = input_node
            return
        
        current_node = self.get_node(index - 1)
        current_next_node = current_node.next
        input_node.next = current_next_node
        current_node.next = input_node
    
    def del_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        current_node = self.get_node(index - 1)
        current_node.next = current_node.next.next
        

test = Linked_list(1)
test.append(2)
test.append(3)
test.append(4)

test.add_node(1, 10)
# test.del_node(0)
test.print_all()