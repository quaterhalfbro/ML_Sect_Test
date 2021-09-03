import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from pprint import pprint
from scipy.spatial.distance import cdist, cosine

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
    v = np.random.randint(0, 10, 5)
    m = np.random.randint(0, 10, (5, 6))
    pprint(v)
    pprint(m)
    n_v = np.reshape(v, (1, 5))
    n_m = np.rot90(m)
    res = n_m[np.argmin(cdist(n_v, n_m, 'cosine'), axis=1)][0]
    print(res, cosine(v, res), sep='\n')

def num3():
    f1 = list(map(lambda x: 1 if x in {4, 5} else 0, range(10)))
    f2 = list(map(lambda x: 1 if x in {1, 2} else 0, range(4)))
    f3 = np.convolve(f1, f2, mode='same')
    print(f3)
    plt.plot(range(len(f3)), f1)
    plt.plot(range(len(f3)), f3)
    plt.show()

num1()
# num2()
# num3()