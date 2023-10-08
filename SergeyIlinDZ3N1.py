import turtle as t
from random import randint
n = 1
t.speed (12)
while n<1000:
    t.forward (randint(5, 50))
    t.left (randint(1, 181))
    n=n+1
t.done