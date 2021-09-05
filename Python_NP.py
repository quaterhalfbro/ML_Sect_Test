import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from pprint import pprint
from matplotlib.animation import FuncAnimation

def num1():
    m = np.random.randint(-9, 9, (10, 10))
    pprint(m)
    m[(m < 5) & (m > -3)] = 1
    pprint(m)
    df = pd.DataFrame(m)
    plt.figure(figsize=(12, 10), dpi=80)
    sns.heatmap(df, xticklabels=df.columns, yticklabels=df.columns, cmap='RdYlGn', center=0, annot=True)
    plt.show()

def num2():
    def cosine(a, b):
        return 1 - sum(np.transpose(a * b)) / (sum(np.transpose(a**2)) * sum(b**2))**0.5

    v = np.random.randint(0, 10, 5)
    m = np.random.randint(0, 10, (5, 6))
    pprint(v)
    pprint(m)
    n_m = np.transpose(m)
    cos_rasts = cosine(n_m, v)
    print(cos_rasts)
    min_rast_index = np.where(cos_rasts == min(cos_rasts))[0][0]
    print(n_m[min_rast_index])
    print(cosine(n_m[min_rast_index], v))

def num3():
    f1, f2 = np.linspace(0, 8, 9), np.linspace(0, 3, 4)
    f1 = np.where((f1 >= 4) & (f1 <= 5), 1, 0)
    f2 = np.where((f2 >= 1) & (f2 <= 2), 1, 0)
    fig, ax = plt.subplots()
    f1_x = np.linspace(0, 8, 90)
    f1_y = np.where((f1_x >= 4) & (f1_x <= 5), 1, 0)
    f2_x = np.linspace(0, 3, 40)
    f2_y = np.where((f2_x >= 1) & (f2_x <= 2), 1, 0)
    f3_y = np.convolve(f1_y, f2_y, mode='same')
    f3_y = f3_y / max(f3_y)
    f3_x = np.linspace(0, 8, len(f3_y))

    def animate(i):
        ax.clear()
        f2_x = np.linspace(i, 3 + i, 40)
        f2_y = np.where((f2_x >= 1 + i) & (f2_x <= 2 + i), 1, 0)
        line1 = ax.plot(f2_x, f2_y)
        line2 = ax.plot(f1_x, f1_y)
        f3_true = np.where(f3_x <= i + 1.5)[0]
        line3 = ax.plot(f3_x[f3_true], f3_y[f3_true])
        return [line1, line2, line3]

    anim = FuncAnimation(fig, animate, frames=np.linspace(0, 6, 210), interval=10, repeat=True)
    plt.show()

# num1()
num2()
# num3()