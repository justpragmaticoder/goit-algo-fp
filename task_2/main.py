import turtle


def draw_branch(branch_length, t, level):
    if level == 0:
        return
    else:
        t.forward(branch_length)
        t.right(20)
        draw_branch(branch_length - 15, t, level - 1)
        t.left(40)
        draw_branch(branch_length - 15, t, level - 1)
        t.right(20)
        t.backward(branch_length)


def main():
    try:
        recursion_level = int(input("Enter recursion level: "))
        screen = turtle.Screen()
        screen.bgcolor("white")

        t = turtle.Turtle()
        t.speed(2)
        t.color("green")
        t.width(2)

        t.left(90)
        draw_branch(80, t, recursion_level)

        screen.exitonclick()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")


if __name__ == "__main__":
    main()
