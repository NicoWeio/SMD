import matplotlib.pyplot as plt
import numpy as np
# from numpy.random import default_rng

rng = np.random.default_rng(42)

# zahlen = rng.uniform(1, 100, 1e5)
# zahlen = rng.integers(1, 100+1, 1e5)
zahlen = rng.integers(1, 100+1, 100000)
zahlen_log = np.log(zahlen)


fig, axs = plt.subplots(2,3)

mat = [
[ 5, 10, 15],
[20, 30, 50],
]

for i, rows in enumerate(mat):
    for k, bins in enumerate(rows):
        axs[i, k].hist(zahlen_log, bins=bins)
plt.show()

plt.hist(zahlen)
# plt.hist(zahlen_log)
plt.show()
