class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        cur, cur2 = self.head, self.head
        cnt, cnt2 = 0, 0
        while 1:
            if cur is None:
                break
            else:
                cur = cur.next
                cnt += 1

        while cnt2 != (cnt - k):
            cur2 = cur2.next
            cnt2 += 1
            
        return cur2


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)

print(linked_list.get_kth_node_from_last(1).data)  # 7이 나와야 합니다!