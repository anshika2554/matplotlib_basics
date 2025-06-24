import matplotlib.pyplot as plt
import numpy as np

values=np.random.normal(90,1.7,1000)
plt.boxplot(values)
plt.show()