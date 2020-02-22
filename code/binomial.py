from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

n = 20
p = 0.5

x = np.linspace(0, n, n + 1)
y = binom.pmf(x, n, p)

plt.bar(x, y)

plt.show()
