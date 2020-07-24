from scipy.stats import gamma
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)

total_divisions = 100000
x = np.linspace(0, 20, total_divisions)

params = [
    { 'p': 1, 'alpha': 0.5 },
    { 'p': 2, 'alpha': 0.5 },
    { 'p': 3, 'alpha': 0.5 },
    { 'p': 5, 'alpha': 1 },
    { 'p': 9, 'alpha': 2 },
    { 'p': 7.5, 'alpha': 1 },
    { 'p': 0.5, 'alpha': 1 },
]

for pAndAlpha in params:
    # See https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.stats.gamma.html
    # and Wikipedia Gamma distribution article to understand the scale parameter
    p = pAndAlpha['p']
    alpha = pAndAlpha['alpha']
    plt.plot(x, gamma.cdf(x, p, scale=1/alpha), label=f'$p = {p}, \\alpha = {alpha}$')

plt.axis([0, 20, 0, 1])
plt.xlabel(r'$x$')
plt.ylabel(r'$F(x)$')
plt.legend()

plt.savefig('../doc/images/r/gamma/cdf.pdf')
