import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
 
country = ('Bahrain','Kuwait','Kazakhstan','Azerbaijan','Uzbekistan')
y_pos = np.arange(len(country))
totalcases = [1767, 1751, 1615, 1340, 1450]
 
plt.barh(y_pos, totalcases, align='center', alpha=0.3)
plt.yticks(y_pos, country)
plt.xlabel('Total Cases')
plt.title('Covid-19 Virus Total Cases')
 
plt.show()