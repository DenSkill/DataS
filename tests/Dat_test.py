from unittest import TestCase, main
from Main.Dat import Node, stack, Stack
import unittest


class DatTest(TestCase):
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')

    def test_data(self):
        self.assertEqual(self.stack.top.data, 'data3')
        self.assertEqual(self.stack.top.next_node.data, 'data2')
        self.assertEqual(self.stack.top.next_node.next_node.data, 'data1')

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 'data3')



if __name__ == '__main__':
    main()
