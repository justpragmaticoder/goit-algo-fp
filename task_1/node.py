class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return dummy.next


def insertion_sort(head):
    if head is None or head.next is None:
        return head

    sorted_list = None
    current = head

    while current is not None:
        next_node = current.next
        sorted_list = sorted_insert(sorted_list, current)
        current = next_node

    return sorted_list


def sorted_insert(head, new_node):
    if head is None or head.data >= new_node.data:
        new_node.next = head
        return new_node

    current = head
    while current.next is not None and current.next.data < new_node.data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head
