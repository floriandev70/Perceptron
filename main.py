# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Plot example with prelearned weights
w0 = -2.0
w1 = -3.5
w2 = 9.2

perc = Perceptron(np.array([w0,w1,w2]))

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

x = np.linspace(1, 10, 100)

plt.plot(x, perc.fh(x), color='red') # new line
plt.show()
