# Ильин Сергей ДЗ 1.3
import numpy as np
import matplotlib.pyplot as plt
x = np.arange (-100, 100, 0.01)
y = np.log((x*x+1)*np.exp(-abs(x)/10))/np.log(1+np.tan(1/(1+np.sin(x)**2)))
plt.plot(x, y, color='purple')
plt.legend(loc='best', fontsize=8)
plt.grid()
plt.show()