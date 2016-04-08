import numpy as np
import matplotlib.pyplot as plt

N = 1000
X = np.sum(np.random.random((N,N))*2-1,axis=1)

plt.hist(X,bins=25)
plt.show()
