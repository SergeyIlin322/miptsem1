import turtle as t
n=0
while n<=100:
    for i in range (4):
        t.forward(n)
        t.left(90)
    t.penup()
    t.right(135)
    t.forward(7)
    t.pendown()
    t.left(135)
    n+=10
t.done()