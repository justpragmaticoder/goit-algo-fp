from binary_tree import Node, draw_binary_heap

heap_root = Node(8)
heap_root.left = Node(6)
heap_root.right = Node(7)
heap_root.left.left = Node(4)
heap_root.left.right = Node(5)
heap_root.right.left = Node(3)

draw_binary_heap(heap_root)
