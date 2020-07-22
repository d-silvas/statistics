from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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

default_cycle_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

# Separate plots
for nAndP in params:
    n = nAndP['n']
    p = nAndP['p']

    x_integers = range(n)

    for x in x_integers:
        y = binom.cdf(x, n, p)
        plt.scatter(x, y, c=default_cycle_colors[0])
        plt.plot([x, x + 1], [y, y], color=default_cycle_colors[0])

    # Save file. This counts on the working directory to be the "code" folder !!!
    pStr = str(p).replace('.', '')
    plt.savefig(f'../doc/images/discrete/binomial/cdf_{n}_{pStr}.pdf')
    plt.close()

# Joint plot
handles = [] # For the legend
for index, nAndP in enumerate(params):
    n = nAndP['n']
    p = nAndP['p']

    x_integers = range(40) # Set max x to plot to 40

    color = default_cycle_colors[index]

    for x in x_integers:
        y = binom.cdf(x, n, p)
        plt.scatter(x, y, c=color)
        plt.plot([x, x + 1], [y, y], color=color)

    handles.append(mpatches.Patch(color=color, label=f'$n = {n}, p = {p}$'))

plt.legend(handles=handles)
plt.savefig('../doc/images/discrete/binomial/cdf_all.pdf')
