import turtle as t
t.color('yellow')
t.begin_fill()
#Делаем основу эмоджи
for i in range (45):
    t.forward(16)
    t.left(8)
t.end_fill()
t.goto(-30, 135)
t.color ('white')
t.begin_fill()
#делаем левый глаз
for i in range (45):
    t.forward(4)
    t.left(8)
t.end_fill()
#делаем правый глаз
t.goto(50, 135)
t.color ('white')
t.begin_fill()
for i in range (45):
    t.forward(4)
    t.left(8)
t.end_fill()
#делаем нос
t.penup()
t.goto(10, 125)
t.right(90)
t.pendown()
t.color ('black')
t.left(0)
t.forward(40)
#Делаем рот
t.penup()
t.goto(-50, 50)
t.left(90)
t.pendown()
t.forward(120)
t.done()