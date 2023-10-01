import matplotlib.pyplot as plt
import numpy as np
def ws(x, a, b, n):
    r = 0
    for z in range(n+1):
        r += b**z*np.cos(np.pi*x*a**z)
    return r

a = 3
b = 0.5
n = 10
x = np.linspace(-5, 5, 1000)

y = ws(x, a, b, n)

plt.plot(x, y)
plt.title("График функции Вейерштрасса")
plt.grid()
plt.show()
