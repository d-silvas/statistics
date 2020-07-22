
from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import rc

rc('text', usetex=True)

max_num = 60
means = [2, 3, 5, 10, 20, 30]

default_cycle_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

# Separate plots
for mean in means:
    x_integers = range(max_num)

    for x in x_integers:
        y = poisson.cdf(x, mean)
        plt.scatter(x, y, c=default_cycle_colors[0])
        plt.plot([x, x + 1], [y, y], color=default_cycle_colors[0])

    plt.savefig(f'../doc/images/discrete/poisson/cdf_{mean}.pdf')
    plt.close()

# Joint plot
handles = []
for index, mean in enumerate(means):
    x_integers = range(max_num)
    color = default_cycle_colors[index]

    for x in x_integers:
        y = poisson.cdf(x, mean)
        plt.scatter(x, y, c=color)
        plt.plot([x, x + 1], [y, y], color=color)

    handles.append(mpatches.Patch(color=color, label=f'$\\lambda = {mean}$'))

plt.legend(handles=handles)
plt.savefig('../doc/images/discrete/poisson/cdf_all.pdf')
