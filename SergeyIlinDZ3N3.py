import turtle as t
x = -350
y = 0
Vx = 0.5
Vy = 2
ay = -0.2
dt = 0.1 

t.tracer(0, 0)
n=1
while n<3000:
    x += Vx * dt
    y += Vy * dt + ay * dt**2 / 2
    Vy += ay * dt
    if y <= 0:
        Vy = -Vy * 0.8
    t.goto(x, y)
    t.update()
    n=n+1
t.done()