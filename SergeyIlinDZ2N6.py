import turtle as t
n=int(input('Введите число лап '))
for i in range (12):
    t.forward(100)
    t.left(180)
    t.stamp()
    t.forward(100)
    t.left(180)
    t.left(360/n)
t.done()