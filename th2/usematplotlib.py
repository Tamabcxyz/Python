import numpy
import matplotlib.pyplot as plt
# plot columns
#x = numpy.random.uniform(0.0, 5.0, 250)
#plt.hist(x, 5)
#plt.show()

#plot dot

X = [590,540,740,130,810,300,320,230,470,620,770,250]
Y = [32,36,39,52,61,72,77,75,68,57,48,48]

#scatter plot, s is size of marker
plt.scatter(X, Y, s=60, c='red', marker='^')

#change axes ranges
#plt.xlim(0,1000)plt.ylim(0,100)

#add title
plt.title('Relationship Between Temperature and Iced Coffee Sales')

#add x and y labels
plt.xlabel('Cups of Iced Coffee Sold')
plt.ylabel('Temperature in Fahrenheit')

#show plot
plt.show()