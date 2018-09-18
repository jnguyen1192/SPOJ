import numpy as np
import math
import matplotlib.pyplot as plt
from PIL import Image


def delta(Smax, Smin, R):
    L = 2 ** R
    return (Smax-Smin)/L


def Q(s, Smin, D):
    return math.floor((s-Smin)/D + 0.5) * D + Smin


def scalar_quantizer(Signal, Smin, D):
    S = [np.array([Q(s, Smin, D)]) for s in Signal]
    return S


def imgsave(i, l, h, SignalFin):
    # create a new img
    res = Image.new("L", (l, h))
    # fill the img
    res.putdata(SignalFin)
    # save the file with his name
    res.save("new"+i)


def quantizer_algorithm(Signal, R):
    Max = np.max(Signal)
    Min = np.min(Signal)
    Delta = delta(Max, Min, R)
    return scalar_quantizer(Signal, Min, Delta)


def plot_img(i):
    # open image
    image = Image.open(i)
    # transform img to signal
    Signal = image.getdata()
    # get size of img
    l, h = image.size

    # Quantizer algorithm
    SignalFin = quantizer_algorithm(Signal, 1)

    imgsave(i, l, h, SignalFin)
'''
def plot(Sign, x):
    Signal = Sign(x)
    Max = np.max(Signal)
    Min = np.min(Signal)
    Delta = delta(Max, Min)

    SignalFin = scalar_quantizer(Signal, Min, Delta)
    plt.plot(Signal)
    plt.plot(SignalFin)
    plt.show()
'''


def D(R):
    image = Image.open('lena512.bmp')
    Signal = image.getdata()
    N = len(Signal)
    print('N ', N)
    SignalFin = quantizer_algorithm(Signal, R)

    return (1.0/N) * sum([abs((Signal[n] - SignalFin[n])) ** 2 for n in range(1, N)])


def distorsion():
    return [D(i) for i in range(1, 8)]


def plot_distorsion():
    plt.plot(distorsion())
    plt.show()

def main():
    #test sin
    #plot(np.sin, np.linspace(-np.pi, np.pi, 201))
    #plot_img('lena512.bmp')
    plot_distorsion()

main()

