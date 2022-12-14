# https://www.notion.so/2-9e5eccb6b7ce4c4ba028dae6ad135830

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)
first_node = Node(5)

node.next = first_node

class LinkedList:
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
        print(cur.data)
        while cur.next is not None:
            print(cur.next.data)
            cur = cur.next

linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)

linked_list.print_all()