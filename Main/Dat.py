class Node:
    def __init__(self,data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:

    def __init__(self):
        self.top = Node()

    def push(self, data):  # создает экземпляр класса node и добавляет его в стэк
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def next_node(self):  # возвращает "ид" следующего элемента в спике
        return self.next_node()

    def top(self):  # возвращает верхний элемент списка
        return self.top()

    def data(self):
        return self.data()

    def pop(self): #удаляет и возвращает верхний элемент стэка
        remove = self.top
        self.top = self.top.next_node
        return remove.data



stack = Stack()
stack.push('data1')
data = stack.pop()

# стэк стал пустой
print(stack.top)
# None

# pop() удаляет элемент и возвращает данные удаленного элемента
print(data)
# 'data1'


stack = Stack()
stack.push('data1')
stack.push('data2')
data = stack.pop()

# теперь последний элемента содержит данные data1
print(stack.top.data)
# 'data1'

# данные удаленного элемента
print(data)
# 'data2'