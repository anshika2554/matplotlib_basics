import matplotlib.pyplot as plt

lang=["python","c++","c#","java","go"]
votes=[34,67,65,32,21]
plt.bar(lang,votes,width=0.5,edgecolor="k", lw=3)
plt.xlabel('Languages')
plt.ylabel("Votes")
plt.show()