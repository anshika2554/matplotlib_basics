import matplotlib.pyplot as plt
import numpy as np

lang=["python","c++","c#","java","go"]
votes=[34,54,32,66,8]
explodes=[0,0,0,0,0.3]
plt.pie(votes,labels=lang, explode=explodes, autopct="%.2f%%") #pctdistance, startangle
#plt.pie(votes,labels=None)
#plt.legend(labels=lang, loc="lower left")
plt.show()