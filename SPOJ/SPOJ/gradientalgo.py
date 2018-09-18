from scipy import misc

import matplotlib.pyplot as plt
import numpy as np

step = 0.5

#----------------------------------------------------------------------------------------#
# Function Definition


def fonction(x):
    return x*x

#----------------------------------------------------------------------------------------#
# Plot function

x = np.arange(-5, 6, step)
y = fonction(x)

plt.plot(x, y,'r-')
#plt.show()

#----------------------------------------------------------------------------------------#
# Gradient Descent


def gradientDescent(step):
    alpha = 0.1 # learning rate
    nb_max_iter = 100 # Nb max d'iteration
    eps = 0.0001 # stop condition

    x0 = 1.5 # start point
    y0 = fonction(x0)
    plt.scatter(x0, fonction(x0))

    cond = eps + 10.0 # start with cond greater than eps (assumption)
    nb_iter = 0
    tmp_y = y0
    while cond > eps and nb_iter < nb_max_iter:
        x0 = x0 - alpha * misc.derivative(fonction, x0)
        y0 = fonction(x0)
        nb_iter = nb_iter + 1
        cond = abs( tmp_y - y0 )
        tmp_y = y0
        print x0,y0,cond
        plt.scatter(x0, y0)

    plt.title("Gradient Descent Python with step = " + str(step))
    plt.grid()

    plt.savefig("gradient_descent_1d_python.png", bbox_inches='tight')
    plt.show()

gradientDescent(step)