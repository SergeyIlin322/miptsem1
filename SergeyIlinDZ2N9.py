import turtle as t
n=3
while n<100:
    for i in range (n):
        t.forward(10*n)
        t.left(360/n)
    t.right(135)
    t.penup()
    t.forward(10)
    t.left(135)
    t.pendown()
    n+=1
t.done()