import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import h5py
import time
sigma = 10
rho = 28
beta = 8/3

def time_derivative(r):
    x, y, z = r
    return np.array([sigma*(y-x), x*(rho-z)-y, x*y-beta*z])

def RK4_step(r, dt, f=time_derivative):
    k1 = f(r)
    k2 = f(r+k1*dt/2)
    k3 = f(r+k2*dt/2)
    k4 = f(r+k3*dt)
    return r + dt/6*(k1+2*(k2+k3)+k4)

NT = 10000
dt=0.01

def run(r, filename="Lorenz.hdf5", NT=NT, dt=dt):
    current_time = time.strftime("%H%M%S") + str(int(1000*np.random.random(1)))
    r_history=np.zeros((NT, *r.shape))
    for i in range(NT):
        r_history[i]=r
        r = RK4_step(r, dt)
    with h5py.File(filename) as f:
        f.create_dataset("r_h_{}".format(current_time), data=r_history)
        f.attrs['sigma_{}'.format(current_time)] = sigma
        f.attrs['rho_{}'.format(rho)] = rho
        f.attrs['beta_{}'.format(beta)] = beta

    return r_history

def find_minima(x, max_distance, where):
    indices = np.abs(x-where) < np.max(np.abs(x-where))*max_distance
    return indices

def plot_full_3d(filename="Lorenz.hdf5"):
    fig = plt.figure(figsize=(11,7), dpi=100)
    axes = fig.gca(projection='3d')

    with h5py.File(filename) as f:
        for dataset in f:
            x = f[dataset][:,0]
            y = f[dataset][:,1]
            z = f[dataset][:,2]
            axes.plot(x,y,z, alpha=0.5)
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    axes.set_zlabel('z')
    axes.set_title('Rownanie Lorenza')
    axes.grid()
    plt.show()

def plot_takens_reconstruction(filename="Lorenz.hdf5", tau = 1, m = 6):
    fig = plt.figure(figsize=(11,7), dpi=100)
    axes = fig.gca(projection='3d')

    with h5py.File(filename) as f:
        for dataset in f:
            x = []
            for n in range(m):
                x.append(f[dataset][n*tau:-(m-n)*tau,0])
            x, y, z = x[0], x[1], x[2]
            print(x.shape, y.shape, z.shape)
            axes.plot(x,y,z, alpha=0.5, label="Rekonstrukcja")

            x = f[dataset][:,0]
            y = f[dataset][:,1]
            z = f[dataset][:,2]
            axes.plot(x,y,z, alpha=0.5, label="Oryginal")
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    axes.set_zlabel('z')
    axes.legend()
    axes.set_title('Rekonstrukcja z Takensa - tau = {}'.format(tau))
    axes.grid()
    plt.show()

def plot_poincare(filename="Lorenz.hdf5", max_distance=0.01, where=0):
    with h5py.File(filename) as f:
        for dataset in f:
            x = f[dataset][:,0]
            y = f[dataset][:,1]
            z = f[dataset][:,2]

            indices = find_minima(x, max_distance, where)
            print(indices)
            plt.plot(y[indices], z[indices], "o")
    plt.xlabel('y')
    plt.ylabel('z')
    plt.title('Przekroj Poincare, rownanie Lorenza, x={}'.format(where))
    plt.grid()
    plt.show()


# def solve_y(C):
#   podpierwiastkiem = 2*np.sqrt(9*C**2 - 3*C) - 6*C +1
#   return 0.5 * (1 + podpierwiastkiem**(1/3) + podpierwiastkiem**(-1/3))

if __name__=="__main__":
    filename = "Lorenz.hdf5"
    for i in range(1):
        print(i)
        r = np.random.random(3)*5
        run(r, filename=filename)
    for tau in range(1,75,3):
        plot_takens_reconstruction(filename, tau=tau)
    # plot_full_3d(filename)
    # plot_poincare("Lorenz.hdf5", max_distance = 0.1)
