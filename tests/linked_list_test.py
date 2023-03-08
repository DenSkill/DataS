from unittest import TestCase, main
from Main.linked_list import LinkedList, Node, ll
import unittest


class Linked_listtest(TestCase):
    ll = LinkedList()
    ll.insert_beginning({'id': 1})
    ll.insert_at_end({'id': 2})
    ll.insert_at_end({'id': 3})
    ll.insert_beginning({'id': 0})


    def test_insert_beginning(self):
        # self.assertEqual(ll.insert_beginning({'id': 1}))
        pass


    def test_insert_at_end(self):
        # self.assertEqual(ll.insert_at_end())
        pass

    def test_print_ll(self):
        self.assertEqual(ll.print_ll(), None)


if __name__ == '__main__':
    main()
