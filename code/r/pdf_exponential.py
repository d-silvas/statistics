from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

# LaTeX setup
rc('text', usetex=True)

total_divisions = 100000

x = np.linspace(0, 5, total_divisions)
y_05 = expon.pdf(x, 0, 0.5)
y_1 = expon.pdf(x, 0, 1)
y_15 = expon.pdf(x, 0, 1.5)
y_3 = expon.pdf(x, 0, 3)

plt.plot(x, y_05, label=r'$\lambda = 0.5$')
plt.plot(x, y_1, label=r'$\lambda = 1$')
plt.plot(x, y_15, label=r'$\lambda = 1.5$')
plt.plot(x, y_3, label=r'$\lambda = 3$')
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.legend()

# plt.show()

# Save file. This counts on the working directory to be the "code" folder !!!
plt.savefig('../doc/images/r/exponential/pdf.pdf')
