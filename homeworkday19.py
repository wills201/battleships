import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

X = range(1,50)
Y = [value * 3 for value in X]

plt.plot(X,Y)

plt.xlabel("x - axis")

plt.ylabel("y - axis")

plt.show()