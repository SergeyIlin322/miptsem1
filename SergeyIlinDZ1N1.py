#Ильин Сергей ДЗ 1.1
import numpy as np
# a = np.e**(1/(np.sin(x)+1))
# b = 5/4+(1/x**15)
# print (np,log(a/b)/np.log(1+x**2))
x = 1
print (np.log((np.e**(1/(np.sin(x)+1)))/(5/4+(1/x**15)))/np.log(1+x**2))
x = 10
print (np.log((np.e**(1/(np.sin(x)+1)))/(5/4+(1/x**15)))/np.log(1+x**2))
x = 1000
print (np.log((np.e**(1/(np.sin(x)+1)))/(5/4+(1/x**15)))/np.log(1+x**2))