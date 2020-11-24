import turtle

turtle.hideturtle()
turtle.tracer(1)
turtle.penup()
turtle.setposition(-380, 300)
turtle.pendown()
turtle.pensize(2)

axiom = "F+F+F+F"
axmTemp = ""
itr = 3
dl = 24

translate = {"+": "+", "-": "-", "F": "F+F-f-F+F", "f": "f"}
for k in range(itr):
    for ch in axiom:
        axmTemp += translate[ch]
    axiom = axmTemp
    axmTemp = ""

turtle.fillcolor("#29BBCC")
turtle.begin_fill()
for ch in axiom:
    if ch == "+":
        turtle.right(45)
        turtle.forward(8)
        turtle.right(45)
    elif ch == "-":
        turtle.left(45)
        turtle.forward(8)
        turtle.left(45)
    else:
        turtle.forward(dl)

turtle.end_fill()
turtle.update()
turtle.mainloop()
