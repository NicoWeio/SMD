import matplotlib.pyplot as plt
import numpy as np

groesse, gewicht = np.genfromtxt('Groesse_Gewicht.txt', unpack=True)


mat = [
[ 5, 10, 15],
[20, 30, 50],
]

for daten, name in [(groesse, 'Größe'), (gewicht, 'Gewicht')]:
    fig, axs = plt.subplots(2,3)
    fig.suptitle(name)
    for i, rows in enumerate(mat):
        for k, bins in enumerate(rows):
            axs[i, k].hist(daten, bins=bins)
plt.show()
