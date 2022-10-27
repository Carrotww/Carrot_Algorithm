class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # 맨 뒤 추가 enqueue(data)
    def enqueue(self, value):
        temp = Node(value)
        if self.is_empty():
            self.head = temp
            self.tail = temp
            return

        self.tail.next = temp
        self.tail = temp
        return

    # 맨 앞 뽑기
    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        temp = self.head
        self.head = self.head.next
        
        return temp.data

    # 맨 앞 데이터 보기
    def peek(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.head.data

    # 큐 확인하기
    def is_empty(self):
        return self.head is None

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q.dequeue())
print(q.peek())
print(q.dequeue())

print(q.is_empty())