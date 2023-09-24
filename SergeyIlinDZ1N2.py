#Ильин Сергей ДЗ1.2
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-15, 16, 0.01)
plt.figure(figsize=(13, 9))
plt.grid()
plt.plot (x, x*x-x-6, label=r'$f(x)=x^2-x-6$', color='purple')
plt.legend(loc='best', fontsize=12)
y=0*x
plt.plot(x, y, color='blue')
plt.show()