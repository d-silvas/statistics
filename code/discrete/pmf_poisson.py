from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)

max_num = 60
means = [2, 3, 5, 10, 20, 30]

# Separate plots
for mean in means:
    x = range(max_num)
    y = poisson.pmf(x, mean)

    plt.bar(x, y)

    plt.savefig(f'../doc/images/discrete/poisson/pmf_{mean}.pdf')
    plt.close()

# Joint plot
for mean in means:
    x = range(max_num)
    y = poisson.pmf(x, mean)

    plt.bar(x, y, label=f'$\\lambda = {mean}$')

plt.legend()
plt.savefig('../doc/images/discrete/poisson/pmf_all.pdf')