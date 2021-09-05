import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from random import randint

def plt1():
    m = np.random.sample(200)  # 1
    m2 = np.random.normal(size=200)  # 2

    def method_mullera():
        s = 0
        while not(0 < s <= 1):
            x, y = (np.random.sample() - 0.5) * 2, (np.random.sample() - 0.5) * 2
            s = x**2 + y**2
        s = (-2 * np.log(s) / s)**0.5
        return (x * s, y * s)

    m3 = np.array([method_mullera() for i in range(100)]).reshape(200)  # 3
    plt.hist(m3)
    plt.show()

def plt3():
    cl1_x_center = randint(0, 10)
    cl1_y_center = randint(0, 10)
    cl2_x_center = randint(0, 10)
    cl2_y_center = randint(0, 10)
    cl3_x_center = randint(0, 10)
    cl3_y_center = randint(0, 10)
    cl1_x = np.array([cl1_x_center + (np.random.sample() - 0.5) * 5 for i in range(50)])
    cl1_y = np.array([cl1_y_center + (np.random.sample() - 0.5) * 5 for i in range(50)])
    cl2_x = np.array([cl2_x_center + (np.random.sample() - 0.5) * 5 for i in range(50)])
    cl2_y = np.array([cl2_y_center + (np.random.sample() - 0.5) * 5 for i in range(50)])
    cl3_x = np.array([cl3_x_center + (np.random.sample() - 0.5) * 5 for i in range(50)])
    cl3_y = np.array([cl3_y_center + (np.random.sample() - 0.5) * 5 for i in range(50)])
    plt.scatter(cl1_x, cl1_y, c='red')
    plt.scatter(cl2_x, cl2_y, c='blue')
    plt.scatter(cl3_x, cl3_y, c='yellow')
    plt.show()


plt3()