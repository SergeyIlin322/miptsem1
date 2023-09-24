import matplotlib.pyplot as plt
import numpy as np
def ws(x, a, b, n):
    r = 0
    for k in range(n+1):
        r += b**k*np.cos(np.pi*x*a**k)
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
