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


if __name__ == '__main__':
    main()
