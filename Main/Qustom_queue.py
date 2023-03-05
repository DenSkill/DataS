class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self, start=None, head=None):
        self.start = start
        self.head = head

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        dequeue_element = self.head
        self.head = self.head.next_node
        return dequeue_element.data

queue = Queue()
queue.enqueue('data1')
queue.enqueue('data2')
queue.enqueue('data3')
print(queue.dequeue())
#data1
print(queue.dequeue())
#data2
print(queue.dequeue())
#data3
print(queue.dequeue())
#None