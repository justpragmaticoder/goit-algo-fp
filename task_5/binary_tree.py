import uuid
from queue import Queue

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


def find_max_depth(node, depth=0):
    if node:
        left_depth = find_max_depth(node.left, depth + 1)
        right_depth = find_max_depth(node.right, depth + 1)
        return max(left_depth, right_depth)
    else:
        return depth


def depth_first_traversal(node, colors, depth=0):
    if node:
        max_depth = find_max_depth(node, depth)
        # Generate a unique color based on depth
        color_intensity = 0.1 + 0.6 * (
            depth / max_depth
        )  # Adjusted depth-based color intensity
        color = (0.1, color_intensity, 0.1)

        # Ensure color values are within the [0, 1] range
        color = tuple(min(max(val, 0), 1) for val in color)

        # Visualization step
        print(f"Visiting node {node.val} with color {color}")
        colors[node.id] = color

        # Recur for left and right subtrees
        depth_first_traversal(node.left, colors, depth + 1)
        depth_first_traversal(node.right, colors, depth + 1)


def to_hex(color):
    return "#{:02x}{:02x}{:02x}".format(
        int(color[0] * 255), int(color[1] * 255), int(color[2] * 255)
    )


def generate_shades(base_color, num_shades):
    shades = []
    for i in range(num_shades):
        shade_factor = (i + 1) / num_shades
        shade = (base_color[0], base_color[1] * shade_factor, base_color[2])
        shades.append(shade)
    return shades


def breadth_first_traversal(root, colors):
    base_color = (0.1, 0.7, 0.1)  # Base color (green in this example)
    num_shades = 5  # Number of shades

    shades_of_green = generate_shades(base_color, num_shades)

    queue = Queue()
    queue.put(root)

    while not queue.empty():
        node = queue.get()

        if node:
            # Use shades of green for each node
            color = to_hex(shades_of_green[node.level % num_shades])

            # Visualization step
            print(f"Visiting node {node.val} with color {color}")
            colors[node.id] = color

            # Enqueue left and right children
            if node.left:
                node.left.level = node.level + 1
                queue.put(node.left)
            if node.right:
                node.right.level = node.level + 1
                queue.put(node.right)


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
