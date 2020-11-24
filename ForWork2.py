import turtle


turtle.hideturtle()
turtle.tracer(10)
turtle.penup()
turtle.setpos(-100, -150)
turtle.pendown()

axiom = "FX"
axmTEmp = ""

itr, dl, angl = 15, 3, 90

translate = {"+": "+", "-": "-", "F": "F", "X": "X+YF+", "Y": "-FX-Y"}
for k in range(itr):
    for ch in axiom:
        axmTEmp += translate[ch]
    axiom = axmTEmp
    axmTEmp = ""
for ch in axiom:
    if ch == "+":
        turtle.right(angl)
    elif ch == "-":
        turtle.left(angl)
    elif ch == "F":
        turtle.forward(dl)
turtle.update()
turtle.mainloop()
