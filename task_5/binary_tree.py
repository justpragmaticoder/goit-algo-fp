import uuid

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def draw_binary_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = [node[1]["color"] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in heap.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def depth_first_traversal(node, colors, depth=0):
    if node:
        # Generate a unique color based on depth
        color = (0.1, 0.1 + 0.6 * depth, 0.1)

        # Ensure color values are within the [0, 1] range
        color = tuple(min(max(val, 0), 1) for val in color)

        # Visualization step
        print(f"Visiting node {node.val} with color {color}")
        colors[node.id] = color

        # Recur for left and right subtrees
        depth_first_traversal(node.left, colors, depth + 1)
        depth_first_traversal(node.right, colors, depth + 1)


def breadth_first_traversal(root, colors):
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node:
            # Generate a unique color based on level
            level = node.level
            main_color = 1 if (0.1 + 0.6 * level) > 1 else 0.5
            color = to_hex((0.1, main_color, 0.1))

            # Visualization step
            print(f"Visiting node {node.val} with color {color}")
            colors[node.id] = color

            # Enqueue left and right children
            if node.left:
                node.left.level = node.level + 1
                queue.append(node.left)
            if node.right:
                node.right.level = node.level + 1
                queue.append(node.right)


def draw_tree(tree_root, traversal_type):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = {}
    if traversal_type == "depth_first":
        depth_first_traversal(tree_root, colors)
    elif traversal_type == "breadth_first":
        tree_root.level = 0
        breadth_first_traversal(tree_root, colors)

    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=list(colors.values()),
    )
    plt.show()
