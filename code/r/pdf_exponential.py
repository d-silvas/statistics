from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

# LaTeX setup
rc('text', usetex=True)

total_divisions = 100000
x = np.linspace(0, 5, total_divisions)

for _lambda in [0.5, 1, 1.5, 3]:
    # See https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.expon.html for scale param
    plt.plot(x, expon.pdf(x, 0, 1/_lambda), label=f'$\\lambda = {_lambda}$')

plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.legend()

# Save file. This counts on the working directory to be the "code" folder !!!
plt.savefig('../doc/images/r/exponential/pdf.pdf')
