import numpy as np
import matplotlib.pyplot as plt
import h5py

def Chirikov_step(r, J, K):
    theta, p = r
    # return np.array([theta + J*p - K*np.sin(theta), J*p-K*np.sin(theta)])%(2*np.pi)
    return np.array([theta + J*p, J*p+K*np.sin(theta)])%(2*np.pi)

NT = 10000

def run(r, filename="Chirikov.hdf5", NT=NT, J=1, K=1, debug=False):
    theta0 = r[0]
    r_history=np.zeros((NT, *r.shape))
    for i in range(NT):
        r_history[i]=r
        r = Chirikov_step(r, J, K)

    with h5py.File(filename) as f:
        f.create_dataset("r_h_{}".format(theta0), data=r_history)

    return r_history

def find_minima(x, max_distance, where):
    indices = np.abs(x-where) < np.max(np.abs(x-where))*max_distance
    return indices


def plot_all_from_file(filename="Chirikov.hdf5", max_distance=0.01, where=0):
    with h5py.File(filename) as f:
        for dataset in f:
            theta = f[dataset][:,0]
            p = f[dataset][:,1]

            # indices = find_minima(x, max_distance, where)
            plt.plot(theta[:-1], theta[1:], "o")
    plt.xlabel('theta_n')
    plt.ylabel('theta_n+1')
    plt.title('Przekroj Poincare, odwzorowanie Chirikova')
    plt.grid()
    plt.show()

# def solve_y(C):
#   podpierwiastkiem = 2*np.sqrt(9*C**2 - 3*C) - 6*C +1
#   return 0.5 * (1 + podpierwiastkiem**(1/3) + podpierwiastkiem**(-1/3))

if __name__=="__main__":
    filename = "Chirikov_dissipation2.hdf5"
    # for i in range(100):
    #     print(i)
    #     r = np.random.random(2)*2*np.pi
    #     run(r, filename)
    plot_all_from_file(filename)
