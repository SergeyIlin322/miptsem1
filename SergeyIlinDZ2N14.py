import turtle as t
n=int(input('Введите число вершин звезды'))
for i in range(n):
    t.right(180-180/n)
    t.forward(200)
t.done()
