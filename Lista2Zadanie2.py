import random
from time import perf_counter
import matplotlib.pyplot as plt

def generate_set(n):
    return set(random.choices(range(2*n), k = n))

for i in range(0, 100001, 1000):
    s1 = generate_set(i)
    s2 = s1.copy()
    # xs.append(i)
    t1_start = perf_counter()
    
    s1 = s1 | {0}

    t1_stop = perf_counter()

    t2_start = perf_counter()

    s2 |= {0}

    t2_stop = perf_counter()

    plt.scatter(i, t1_stop - t1_start, c = 'black', s=10)
    plt.scatter(i, t2_stop - t2_start, c = 'red', s = 10)

plt.show()

