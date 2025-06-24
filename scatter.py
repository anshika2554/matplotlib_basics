import matplotlib.pyplot as plt 
import numpy as np

#chart1
xdata= np.random.random(20)*100
ydata= np.random.random(20)*100  #size of x and y must be same
plt.scatter(xdata,ydata, c="red",s=50,marker="o") #c for color s for size alpha for transparency
plt.show()

#chart2
xdata=np.random.random(1000)*1000
ydata=np.random.random(1000)*1000
plt.scatter(xdata,ydata, marker="*", alpha=0.3, s=150)
plt.show()

#chart3
#for giving different color to each dot use "c" instead of color
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
plt.scatter(x, y, c=colors)
plt.show()