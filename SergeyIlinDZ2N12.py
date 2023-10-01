import turtle as t
n=1
t.left(90)
while n<11:
    for i in range (45):
        t.forward(5)
        t.left(4)
    for i in range (45):
        t.forward(1)
        t.left(4)
    n+=1
t.done()