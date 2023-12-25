import numpy as np
import matplotlib.pyplot as plt
x = np.random.uniform(0.0, 5.0, 100)
y = np.random.normal(5.0, 10000000, 100)
plt.scatter(x=x, y=y)
plt.plasma()
plt.show()
