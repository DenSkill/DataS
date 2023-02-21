class Node:
    def __init__(self,data=None):
        self.data = data
        self.next_node = None


class Stack:

    def __init__(self):
        self.top = Node()

    def push(self, data):  # создает экземпляр класса node и добавляет его в стэк
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def next_node(self):  # возвращает "ид" следующего элемента в спике
        return self.next_node()

    def top(self):  # возвращает верхний элемент списка
        return self.top()

    def data(self):
        return self.data()



stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')
print(stack.top.data)
print(stack.top.next_node.data)
print(stack.top.next_node.next_node.data)
print(stack.top.next_node.next_node.next_node)
print(stack.top.next_node.next_node.next_node.data)
