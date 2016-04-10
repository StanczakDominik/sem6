import numpy as np
import matplotlib.pyplot as plt
import h5py
def V_x(x, y):
    return 0.5*(2*x+4*x*y)
def V_y(x, y):
    return 0.5*(2*y+2*x**2-2*y**2)

def time_derivative(r):
    x, y, vx, vy = r
    return np.array([vx, vy, -V_x(x,y), -V_y(x,y)])

def RK4_step(r, dt, f=time_derivative):
    k1 = f(r)
    k2 = f(r+k1*dt/2)
    k3 = f(r+k2*dt/2)
    k4 = f(r+k3*dt)
    return r + dt/6*(k1+2*(k2+k3)+k4)

def E(r):
    x, y, vx, vy = r
    return 0.5*(x**2 + y**2 + 2*x**2*y - 2*y**3/3 + vx**2 + vy**2)

NT = 100000
dt=0.1

def run(r, filename="HenonHeiles.hdf5", NT=NT, dt=dt, debug=False):
    r_history=np.zeros((NT, *r.shape))
    E_start = E(r)
    if debug:
        print(E_start)
    for i in range(NT):
        r_history[i]=r
        r = RK4_step(r, dt)
    E_finish = E(r)
    if debug:
        print(E_finish)

    with h5py.File(filename) as f:
        f.create_dataset("r_h_{}".format(E_start), data=r_history)
        f.attrs['E_s_{}'.format(E_start)] = E_start
        f.attrs['E_f_{}'.format(E_start)] = E_finish

    return r_history

def find_minima(x, max_distance, where):
    indices = np.abs(x-where) < np.max(np.abs(x-where))*max_distance
    return indices


def plot_all_from_file(filename="HenonHeiles.hdf5", max_distance=0.01, where=0):
    with h5py.File(filename) as f:
        for dataset in f:
            x = f[dataset][:,0]
            y = f[dataset][:,1]
            vx = f[dataset][:,2]
            vy = f[dataset][:,3]

            indices = find_minima(x, max_distance, where)
            plt.plot(y[indices], vy[indices], "o")
    plt.xlabel('y')
    plt.ylabel('vy')
    plt.title('Przekroj Poincare, rownanie Henona-Heilesa, x={}'.format(where))
    plt.grid()
    plt.show()

# def solve_y(C):
#   podpierwiastkiem = 2*np.sqrt(9*C**2 - 3*C) - 6*C +1
#   return 0.5 * (1 + podpierwiastkiem**(1/3) + podpierwiastkiem**(-1/3))

if __name__=="__main__":
    # En = 1/8
    plot_all_from_file("HenonHeiles.hdf5", where=0)
    # for i in range(100):
    #     print(i)
    #     r = np.random.random(4)*0.25
    #     # r = np.zeros(4)
    #     # xdot, ydot = np.random.random(2)*0.25
    #     # C = 2*En - 0.5*(xdot**2 + ydot**2)
    #     # print(C)
    #     # r[1] = solve_y(C)
    #     # if np.isnan(r[1]):
    #     #     continue
    #     # r[2:] = xdot, ydot
    #     # print(r)
    #     # #pick xdot, vdot at random
    #     # #E = 0.5 (y**2 - 2/3 y**3 + Venergy)
    #     # #2E - V_energy = y**2 - 2/3 y**3
    #     # #def energy(y, constant = 2E-V_energy):
    #     # #   return y**2 - 2/3*y**3 - constant
    #     # # http://www.wolframalpha.com/input/?i=solve+y%5E2+-+2%2F3*y%5E3+-+C+%3D+0+for+y
    #
    #     run(r, filename="HenonHeiles.hdf5")
