from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)

params = [
    { 'n': 20, 'p': 0.1 },
    { 'n': 20, 'p': 0.5 },
    { 'n': 20, 'p': 0.25 },
    { 'n': 20, 'p': 0.75 },
    { 'n': 100, 'p': 0.1 },
    { 'n': 100, 'p': 0.25 },
]

# Separate plots
for nAndP in params:
    n = nAndP['n']
    p = nAndP['p']

    x = np.linspace(0, n, n + 1)
    y = binom.pmf(x, n, p)

    plt.bar(x, y)

    # Save file. This counts on the working directory to be the "code" folder !!!
    pStr = str(p).replace('.', '')
    plt.savefig(f'../doc/images/discrete/binomial/pmf_{n}_{pStr}.pdf')
    plt.close()

# Joint plot
for nAndP in params:
    n = nAndP['n']
    p = nAndP['p']

    x = np.linspace(0, 40, 41) # Set max x to plot to 40
    y = binom.pmf(x, n, p)

    plt.bar(x, y, label=f'$n = {n}, p = {p}$')

plt.legend()
plt.savefig('../doc/images/discrete/binomial/pmf_all.pdf')
