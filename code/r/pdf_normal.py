from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

total_divisions = 10000000

x = np.linspace(-4, 4, total_divisions)
y = norm.pdf(x)

plt.plot(x, y)

plt.show()
