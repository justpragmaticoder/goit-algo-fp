import turtle


def draw_pythagoras_tree(tree, branch_length, angle, scale, level):
    if level == 0:
        return
    else:
        tree.forward(branch_length)
        tree.left(angle)
        draw_pythagoras_tree(tree, branch_length * scale, angle, scale, level - 1)
        tree.right(2 * angle)
        draw_pythagoras_tree(tree, branch_length * scale, angle, scale, level - 1)
        tree.left(angle)
        tree.backward(branch_length)


def main():
    try:
        recursion_level = int(input("Enter recursion level (height of the tree): "))
        screen = turtle.Screen()
        screen.bgcolor("white")

        tree = turtle.Turtle()
        tree.speed(500)
        tree.color("green")
        tree.width(2)

        tree.left(90)

        start_angle = 25
        scale = 0.7
        start_tree_length = 120

        draw_pythagoras_tree(
            tree, start_tree_length, start_angle, scale, recursion_level
        )

        screen.exitonclick()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")


if __name__ == "__main__":
    main()
