from unittest import TestCase, main
from Main.linked_list import LinkedList, Node, ll
import unittest
from io import StringIO
from contextlib import redirect_stdout


class Linked_listtest(TestCase):

    def test_print_ll(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        expected_output = "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"
        f = StringIO()
        with redirect_stdout(f):
            ll.print_ll()
        self.assertEqual(f.getvalue().strip(), expected_output)

    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        lst = ll.to_list()
        self.assertEqual(len(lst), 4)
        self.assertEqual(lst[0]['id'], 0)
        self.assertEqual(lst[3]['id'], 3)

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
        self.assertEqual(ll.get_data_by_id(2), {'id': 2, 'username': 'mosh_s'})
        self.assertEqual(ll.get_data_by_id(3), None)


if __name__ == '__main__':
    main()
