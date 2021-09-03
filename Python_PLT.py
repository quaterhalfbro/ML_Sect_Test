import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

def plt1():
    m = np.random.sample(200) * 100  # 1
    m2 = np.random.uniform(0, 100, 200)  # 2
    m3 = np.array(list(map(lambda x: x / 2.1 + np.random.sample() * 6, range(200))))
    plt.hist(m)
    plt.show()

def plt3():
    cl1_x = np.array([10 + (np.random.sample() - 0.5) * 5 for i in range(50)])
    cl1_y = np.array([5 + (np.random.sample() - 0.5) * 5 for i in range(50)])
    cl2_x = np.array([2.5 + (np.random.sample() - 0.5) * 5 for i in range(50)])
    cl2_y = np.array([2.5 + (np.random.sample() - 0.5) * 5 for i in range(50)])
    cl3_x = np.array([7 + (np.random.sample() - 0.5) * 5 for i in range(50)])
    cl3_y = np.array([8 + (np.random.sample() - 0.5) * 5 for i in range(50)])
    plt.scatter(cl1_x, cl1_y, c='red')
    plt.scatter(cl2_x, cl2_y, c='blue')
    plt.scatter(cl3_x, cl3_y, c='yellow')
    plt.show()

plt3()