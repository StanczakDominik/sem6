import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt
import matplotlib.cm
import matplotlib.animation as anim

#McCulloch-Pitts neuron model
activationFunctions = {"sgn": lambda x: (np.sign(x)+1)*0.5}

def neuronState(h, T, f):
    """returns vector of neuron state
    h: local field in current iteration
    T: activation threshold
    f: activation function
    """
    return f(h-T)

def fuzzyNeuronState(h, beta):
    probabilitySpinUp = 0.5 * (1 + sp.erf(beta*h))
    random_numbers = np.random.random(h.shape)
    result = -np.ones(h.shape)
    result[random_numbers<probabilitySpinUp] = 1
    return result

def localField(J, s):
    """return vector of local field
    J: matrix of connections between neurons
    s: vector of neuron state in previous iteration"""
    return J@s

if __name__=="__main__":

    hitler = -2*np.array([
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1]
        ])-1
    smiley = -2*np.array([
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0]
        ])-1
    N = 25
    Nax = 5
    images = [hitler, smiley]
    vectors = [image.reshape(N) for image in images]
    outers = [np.outer(vector, vector)/N for vector in vectors]
    synaptic_array = np.sum(outers,axis=0)
    NT = 10
    J = synaptic_array
    J[N-1,0] = J[0,N-1] = -1
    s = np.random.random(N)
    T = np.zeros(N)
    beta = 0.3
    f = activationFunctions["sgn"]
    print("J:\n{}".format(J))

    fig, axes = plt.subplots()
    IM = axes.imshow(hitler, interpolation='nearest', cmap='gray', vmin=0, vmax=1)
    text = axes.text(2,2, "i =", color=[0,0,0,1])
    s = np.random.random(N)
    def init():
        IM.set_array(hitler)
        text.set_text("i =")
        return IM, text
    def animate(i):
        global h, s
        h = localField(J, s)
        s = fuzzyNeuronState(h, beta)
        print(s)
        IM.set_array((-2*s-1).reshape((Nax,Nax)))
        text.set_text("i = {}".format(i))
        return IM, text
    animation = anim.FuncAnimation(fig, animate, interval=1000, frames=NT, blit=True, init_func=init)
    plt.show()
