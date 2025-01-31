from scipy.optimize import fmin
import numpy as np
import matplotlib.pylab as plt

#ax+b=y
x = np.array([2.2, 4.3, 5.1, 5.8, 6.4, 8.0])
y = np.array([0.4, 10.1, 14.0, 10.9, 15.4, 18.5])

sse = lambda a,x,y: np.sum((a[0] + a[1]*x-y) **2)
a, b = fmin(sse, [0,1], args=(x,y))
plt.plot(x,y,'ro')
plt.plot([0,10], [a, a+b*10], alpha=0.8)
for xi, yi in zip(x, y): #zip is function that combines x and y
    plt.plot([xi]*2, [yi, a+b*xi], 'k:')

sae = lambda a,x,y:np.sum(abs(a[0] + a[1]*x-y))
a, b = fmin(sae, [0,1], args=(x,y))
plt.plot(x,y,'ro')
plt.plot([0,10], [a, a+b*10], alpha=0.8)
for xi, yi in zip(x, y): #zip is function that combines x and y
    plt.plot([xi]*2, [yi, a+b*xi], 'k:')

plt.xlim(2, 9)
plt.ylim(0, 20)
plt.gca()
plt.show()