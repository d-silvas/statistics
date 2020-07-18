from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)

total_divisions = 100000
x = np.linspace(0, 5, total_divisions)

for _lambda in [0.5, 1, 1.5, 3]:
    plt.plot(x, expon.cdf(x, 0, 1/_lambda), label=f'$\\lambda = {_lambda}$')

plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.legend()

plt.savefig('../doc/images/r/exponential/cdf.pdf')
