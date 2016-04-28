import numpy as np
import matplotlib.pyplot as plt
Nbins = 20
Nparticles = 100

average_limit = 2*Nparticles/Nbins

r = np.random.randint(0,int(Nbins/2), Nparticles)
bin_y, bin_x = np.histogram(r, bins = Nbins)
hits = bin_y > average_limit
bin_x = bin_x[:-1]
def plot(bin_x, bin_y, hits):
    bin_x_step = 2*( bin_x[1]-bin_x[0])
    plt.bar(bin_x, bin_y, width=bin_x_step)
    plt.bar(bin_x[hits], bin_y[hits], width=bin_x_step, color=[1,0,0,1])
    plt.plot(bin_x, np.ones_like(bin_x)*average_limit)
    plt.show()
plot(bin_x, bin_y, hits)
bin_y[hits+1] += bin_y[hits] #nie +1
bin_y[hits] = 0
plot(bin_x, bin_y, hits)
