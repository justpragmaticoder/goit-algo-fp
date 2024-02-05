from binary_tree import Node, draw_tree


# Creating a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

# Visualizing depth-first traversal
draw_tree(root, "depth_first")

# Visualizing breadth-first traversal
draw_tree(root, "breadth_first")
