from unittest import TestCase, main
from Main.Qustom_queue import Node, Queue
import unittest


class Custom_queuetest(TestCase):

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')
        self.assertEqual(queue.tail.next_node, None)


if __name__ == '__main__':
    main()
