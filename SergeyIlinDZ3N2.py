import turtle as t
t.speed (10)
t.penup ()
t.goto (-350, 0)
t.pendown ()
def draw(n):
    if n == 0: 
        t.forward(50)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.penup()
        t.forward(100)
        t.pendown()

    elif n == 1:
        t.penup()
        t.right(90)
        t.forward(50)
        t.left(135)
        t.pendown()
        t.forward(70)
        t.right(135)
        t.forward(100)
        t.penup()
        t.left(180)
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.pendown()

    elif n == 2: 
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(45)
        t.forward(70)
        t.left(135)
        t.forward(50)
        t.penup()
        t.left(90)
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.pendown()
    
    elif n == 3: 
        t.forward(50)
        t.right(135)
        t.forward(70)
        t.left(135)
        t.forward(50)
        t.right(135)
        t.forward(70)
        t.penup()
        t.left(135)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.right(90)
        t.pendown()

    elif n == 4: 
        t.right(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.left(180)
        t.forward(100)
        t.penup()
        t.right(90)
        t.forward(50)
        t.pendown()

    elif n == 5: 
        t.forward(50)
        t.left(180)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.penup()
        t.left(180)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.right(90)
        t.pendown()

    elif n == 6: 
        t.penup()
        t.forward(50)
        t.pendown()
        t.right(135)
        t.forward(70)
        t.left(45)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.penup()
        t.right(180)
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.right(90)
        t.pendown()

    elif n == 7:
        t.forward(50)
        t.right(135)
        t.forward(70)
        t.left(45)
        t.forward(50)
        t.penup()
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.right(90)

    elif n == 8:
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.left(180)
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.penup()
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.pendown()

    elif n == 9:
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.left(180)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.right(135)
        t.forward(70)
        t.penup()
        t.left(135)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.right(90)
        t.pendown()        

for i in input():
    draw(int(i))
t.done()