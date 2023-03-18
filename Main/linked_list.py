class Node:  # хранит полезные данные (словарь с данными) и ссылку на следующий узел
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:  # хранит ссылку на начало связанного списка и на его конец, т.е. на первый и последний Node.
    def __init__(self, tail=None, head=None):
        self.tail = tail
        self.head = head

    def insert_beginning(self,
                         x):  # принимает данные(словарь) и добавляет узел с этими данными в начало связанного списка
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, x):  # принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)

    def to_list(self):
        """возвращает список с данными, содержащимися в односвязном списке"""
        list_of_contents = []
        current = self.head
        while current is not None:
            list_of_contents.append(current.data)
            current = current.next_node
        return list_of_contents

    def get_data_by_id(self, id):
        """возвращает первый найденный в LinkedList словарь с ключом id, значение которого равно переданному в метод значению"""
        list_of_contents = self.to_list()
        for item in list_of_contents:
            try:
                if type(item) == dict:
                    if item['id'] == id:
                        return item
                else:
                    raise Exception
            except Exception:
                print('Данные не являются словарем или в словаре нет id')


ll = LinkedList()

ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
ll.insert_beginning({'id': 0, 'username': 'serebro'})

# метод to_list()
lst = ll.to_list()
for item in lst: print(item)
# {'id': 0, 'username': 'serebro'}
# {'id': 1, 'username': 'lazzy508509'}
# {'id': 2, 'username': 'mik.roz'}
# {'id': 3, 'username': 'mosh_s'}
# get_data_by_id()
user_data = ll.get_data_by_id(3)
print(user_data)
#{'id': 3, 'username': 'mosh_s'}

# работа блока try/except
ll = LinkedList()
ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
ll.insert_at_end('idusername')
ll.insert_at_end([1, 2, 3])
ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

user_data = ll.get_data_by_id(2)
#Данные не являются словарем или в словаре нет id.
#Данные не являются словарем или в словаре нет id.
print(user_data)
#{'id': 2, 'username': 'mosh_s'}
