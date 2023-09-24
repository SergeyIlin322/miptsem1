import numpy as np
import matplotlib.pyplot as plt
with plt.xkcd():
    function = input("Введите функцию: ")
    x = range(-10, 11)
    y = [eval(function) for x in x]

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции')
    plt.show()