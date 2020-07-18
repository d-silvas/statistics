from scipy.special import gamma
import numpy as np
import matplotlib.pyplot as plt

min_x = 0
max_x = 6
total_points = 10000

x = np.linspace(min_x, max_x, total_points)
y = gamma(x)

plt.ylim(0, 30)
plt.plot(x, y)
plt.savefig(f'../doc/images/appendices/gamma.pdf')
