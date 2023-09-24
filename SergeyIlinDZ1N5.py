import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]

p1, v1 = np.polyfit(x, y, deg=1, cov=True)
p2, v2 = np.polyfit(x, y, deg=2, cov=True)

plnm1 = np.poly1d(p1)
plnm2 = np.poly1d(p2)

plt.errorbar(x, y, xerr=0, yerr=0.1, fmt='o', label='Данные с погрешностями')
plt.plot(x, plnm1(x), label='Полином первой степени')
plt.plot(x, plnm2(x), label='Полином второй степени')
plt.legend()
plt.grid()
plt.show()