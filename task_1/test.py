import unittest
from node import Node, reverse_linked_list, insertion_sort, sorted_insert


class Test(unittest.TestCase):
    def test_reverse_linked_list(self):
        node1 = Node(1)
        node2 = Node(3)
        node3 = Node(5)

        list = node1
        node1.next = node2
        node2.next = node3

        reversed_list = reverse_linked_list(list)
        result = []

        while reversed_list is not None:
            result.append(reversed_list.data)
            reversed_list = reversed_list.next

        self.assertEqual(result, [5, 3, 1])

    def test_insertion_sort(self):
        node1 = Node(2)
        node2 = Node(1)
        node3 = Node(4)
        node4 = Node(2)
        node5 = Node(7)
        node6 = Node(6)

        list = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6

        sorted_list = insertion_sort(list)
        result = []

        while sorted_list is not None:
            result.append(sorted_list.data)
            sorted_list = sorted_list.next

        self.assertEqual(result, [1, 2, 2, 4, 6, 7])

    def test_sorted_insert(self):
        node1 = Node(1)
        node2 = Node(3)
        node3 = Node(5)

        node4 = Node(2)
        node5 = Node(1)
        node6 = Node(4)
        node7 = Node(2)
        node8 = Node(7)
        node9 = Node(6)
        node10 = Node(8)
        node11 = Node(18)

        list = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6

        list2 = node9
        node7.next = node10
        node8.next = node11

        sorted_list = sorted_insert(list, list2)
        result = []

        while sorted_list is not None:
            result.append(sorted_list.data)
            sorted_list = sorted_list.next

        self.assertEqual(result, [1, 3, 5, 2, 1, 4, 6])
