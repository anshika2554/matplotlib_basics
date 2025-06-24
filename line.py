import matplotlib.pyplot as plt
import numpy as np

#chart 1 - sine wave
x = np.arange(100)
plt.plot(x, np.sin(x))
plt.title("Sine Wave")
plt.show()

#chart2
x=2000
years= [2006 + x for x in range(16)]
weight= np.random.random(16)*100
plt.plot(years,weight, c="red",lw=3, linestyle="--") # also can write color and style together in short as r--
plt.show()


#Chart 3 - income chart
years=[2014,2015,2016,2017,2018,2019,2020,2021]
income=[55,56,62,61,72,72,73,75]
income_sec=[52,54,59,62,66,70,73,79]

income_ticks=list(range(50,81,2))

plt.plot(years,income , label="person1")
plt.plot(years,income_sec, label="person2")
plt.title("Income of John(in USD)", fontsize=40, fontname='serif')
plt.xlabel("years")
plt.ylabel("income ove years in USD")
plt.legend(loc="upper right")
plt.yticks(income_ticks,[f"{x}k" for x in income_ticks])
plt.show()


#Chart4
xpoints=np.array([1,3,4,8])
plt.plot(xpoints)
plt.show()

#Chart5
ypoints=np.array([1,3,4,8])
plt.plot(ypoints,"o",mec="k",mfc="r")   # marker edge color, marker face color
plt.show()

#chart6
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.grid(ls="--", color="g", lw=1) #axis="y or x " to show onlu one axis grid also can give styling to it
plt.show()
