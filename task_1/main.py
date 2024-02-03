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


node1 = Node(1)
node2 = Node(3)
node3 = Node(5)

node4 = Node(2)
node5 = Node(4)
node6 = Node(6)

node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

list1 = node1
node1.next = node2
node2.next = node3

list2 = node4
node4.next = node5
node5.next = node6

list3 = node7
node7.next = node8
node8.next = node9

# Реверсуємо list1
reversed_list1 = reverse_linked_list(list1)

# Сортуємо list2 за допомогою сортування вставками
sorted_list2 = insertion_sort(list2)

# Об'єднуємо відсортовані list2 та list3
merged_list = merge_sorted_lists(sorted_list2, list3)

# Виведемо результати
print("Reversed list1:", end=" ")
while reversed_list1 is not None:
    print(reversed_list1.data, end=" ")
    reversed_list1 = reversed_list1.next

print("\nSorted list2:", end=" ")
while sorted_list2 is not None:
    print(sorted_list2.data, end=" ")
    sorted_list2 = sorted_list2.next
