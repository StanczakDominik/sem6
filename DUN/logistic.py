import numpy as np
import matplotlib.pyplot as plt

x = 0.3
x_min = 2.9
N=1000
N_potential = 2**8
N_zlozenia = 3
r = np.linspace(x_min, 4, 10000)

def bernoulli(x, r):
    return (r*x)%1
def tent(x, a):
    return a*(1-2*np.abs(0.5-x))

def logistic(x, r):
    return r*x*(1-x)


def Histogram(x_0=x, r=3.2, NT=N, Map=logistic, N_zlozenia = N_zlozenia):
    a = r
    x_grid = np.linspace(0,1,10000)
    y_grid = x_grid
    for j in range(N_zlozenia):
        y_grid = Map(y_grid, a)
    x = x_0
    xl = np.zeros(NT)
    for i in range(NT):
        xl[i]=x
        for j in range(N_zlozenia):
            x = Map(x, a)

    fig2, (axes2, axes2_position, axes2_time) = plt.subplots(3, figsize=(14,16))
    axes2.set_xlabel('$x_n$')
    axes2.set_ylabel('$x_{n+1}$')
    axes2.plot(x_grid, y_grid, 'k--', label='Map($x_n$, $r={}$)'.format(a))
    axes2.plot(x_grid, x_grid, 'k-', label='$x_n$')
    axes2.scatter(xl[:-1], xl[1:], c = np.linspace(0,1,NT-1), s = 100, label='$x$')
    axes2.grid()
    axes2.set_xlim(0,1)
    axes2.set_ylim(0,1)
    axes2.legend()

    axes2_position.set_xlabel('$n$')
    axes2_position.set_ylabel('$x_{n}$')
    axes2_position.set_ylim(0,1)
    axes2_position.plot(xl, 'k,', label='$x_n$')
    axes2_position.grid()
    axes2_position.legend()

    axes2_time.set_xlabel("pozycja $x_n$")
    axes2_time.set_ylabel("jaki ulamek czasu $x_n$ spedzil w tym miejscu")
    axes2_time.hist(xl, 50, normed=True)
    axes2_time.grid()
    plt.show()
    #return xl

def calculate_orbits(r, x0, N=1000, N_potential=32, N_zlozenia=1, Map = logistic):
    iteration_vector = x0*np.ones_like(r)
    iteration_history = np.zeros((N_potential, r.shape[0]))
    for i in range(N):
        for j in range(N_zlozenia):
            iteration_vector = Map(iteration_vector, r)
        k = i - (N-N_potential)
        if k >= 0:
            iteration_history[k] = iteration_vector
    return iteration_history

def draw_orbits(x_min = x_min, x=x, N=N, N_potential=N_potential, N_zlozenia=N_zlozenia, Map=logistic):
    r = np.linspace(x_min, 4, 1000)
    for orbit in calculate_orbits(r.copy(), x, N, N_potential, N_zlozenia, Map):
        # print(orbit)
        plt.plot(r, orbit, "g,", alpha=0.3)
    plt.title("Diagram bifurkacyjny Mapy logistycznej")
    plt.grid()
    plt.ylabel("$x_N$ od N={} do N={} iteracji".format(N-N_potential, N))
    plt.xlabel("r")
    plt.xlim(x_min,4)
    plt.show()

if __name__=="__main__":
    Histogram(r=3.827, Map=logistic, N_zlozenia =3, x_0 = 0.163157)
    # draw_orbits(r, x, N)
