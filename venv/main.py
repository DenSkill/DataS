class Node:
    def __int__(self, data=None, next_node=None):
        self.data = data
        self.next_node = None


class Stack:

    def __int__(self):
        self.head = Node

    def push(self, data):  # создает экземпляр класса node и добавляет его в стэк
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def next_node(self):  # возвращает "ид" следующего элемента в спике
        return

    def top(self):  # возвращает верхний элемент списка
        return self.head

    def data(self):
        elems = []
        cure_node = self.head
        while cure_node.next != None:
            cure_node = cure_node.next
            elems.append(cure_node.data)
        print(elems)


stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')
print(stack.top.data)
print(stack.top.next_node.data)
print(stack.top.next_node.next_node.data)
print(stack.top.next_node.next_node.next_node)
print(stack.top.next_node.next_node.next_node.data)
