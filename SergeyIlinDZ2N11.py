import turtle as t
n=1
t.left(90)
while n<11:
    for i in range (45):
        t.forward(n)
        t.left(8)
    for i in range (45):
        t.forward(n)
        t.right(8)
    n+=1
t.done()