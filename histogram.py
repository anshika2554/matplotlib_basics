import matplotlib.pyplot as plt
import numpy as np

x=np.random.normal(20,1.5,1000)
plt.hist(x,bins=15, histtype='bar', color='red') # for cumulative write cumulative=true
plt.show()