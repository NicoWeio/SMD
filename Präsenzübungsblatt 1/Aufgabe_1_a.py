import matplotlib.pyplot as plt
import numpy as np

groesse, gewicht = np.genfromtxt('Groesse_Gewicht.txt', unpack=True)

fig, axs = plt.subplots(2,3)

mat = [
[ 5, 10, 15],
[20, 30, 50],
]

for i, rows in enumerate(mat):
    print(i, rows)
    for k, bins in enumerate(rows):
        axs[i, k].hist(groesse, bins=bins)
plt.show()
