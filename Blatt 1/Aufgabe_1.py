import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x**3 + 1/3) - (x**3 - 1/3)
def g(x):
    return ((3 + x**3/3) - (3 - x**3/3)) / x**3

data = [
(f, 'f', {32: (1e1, 1e3), 64: (1e4, 1e6)}),
(g, 'g', {32: (1e-3, 1e-1), 64: (1e-6, 1e-4)}),
]

for precision in [32, 64]:
    print(f"Präzision: {precision}")
    for function, name, lims in data:
        print(f"{name}:")
        x = np.geomspace(*lims[precision], num=10000, dtype=f'float{precision}')
        vals = function(x)
        plt.figure()
        plt.plot(x, vals, label=f'{name}(x)')
        plt.axhline(2/3, color='black')
        plt.xscale('log')

        # Abweichungen um 1%
        algebraic = 2/3
        max_diff = algebraic / 100

        indices1 = x[abs(vals - algebraic) > max_diff]
        print(f"Abweichungen um 1%:\n{indices1[0]} bis {indices1[-1]}")

        # =0
        indices2 = x[vals == 0]
        print(f"= 0:\n{indices2[0]} bis {indices2[-1]}")

        plt.axvspan(indices1[0], indices1[-1], alpha=0.25, color='red', label="Abweichungen um 1%")
        plt.axvspan(indices2[0], indices2[-1], alpha=0.25, color='yellow', label="= 0")
        plt.legend()
        # plt.savefig(f'{name}_{precision}.pdf')
        plt.show()

        print('\n')
