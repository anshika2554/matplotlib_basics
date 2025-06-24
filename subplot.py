import matplotlib.pyplot as plt
import numpy as np

#Plot 1

#subplot 1
x=np.array([2,3,4,6,7])
y=np.array([6,8,3,6,9])

plt.subplot(1,2,1) #row,coloumn,index to have two plots side by side
plt.plot(x,y,marker="o")
plt.title("SALES")

#subplot 2

x1=np.array([5,6,2,3,4])
y1=np.array([8,5,3,7,9])

plt.subplot(1,2,2)
plt.plot(x1,y1, marker='o')
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()


# subplot 1
x=np.array([2,3,4,6,7])
y=np.array([6,8,3,6,9])

plt.subplot(2,1,1) #row,coloumn,index to have two graphs up and down
plt.plot(x,y)

# subplot 2

x1=np.array([5,6,2,3,4])
y1=np.array([8,5,3,7,9])

plt.subplot(2,1,2)
plt.plot(x1,y1)
plt.show()

#Plot 3
x=np.arange(100)

fig,axs=plt.subplots(2,2) #we have 4 axes 00 01 10 11

axs[0,0].plot(x,np.sin(x))
axs[0,0].set_title("Sine wave")

axs[0,1].plot(x,np.cos(x))
axs[0,1].set_title("Cosine wave")

axs[1,0].plot(x,np.random.random(100))
#axs[1,0].set_title("Random wave")

axs[1,1].plot(x,np.log(x))
#axs[1,1].set_title("Log Function")

fig.suptitle("four plots")
plt.show()