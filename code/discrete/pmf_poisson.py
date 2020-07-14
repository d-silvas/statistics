from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt

max_num = 60
mean = 30

x = range(max_num)
y = poisson.pmf(x, mean)

plt.bar(x, y)

plt.show()
