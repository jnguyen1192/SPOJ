import numpy as np
import math
import matplotlib.pyplot as plt
from PIL import Image


R = 1
L = 2 ** R


def delta(Smax, Smin):
    return (Smax-Smin)/L


def Q(s, Smin, D):
    return math.floor((s-Smin)/D + 0.5) * D + Smin


def scalar_quantizer(Signal, Smin, D):
    S = [np.array([Q(s, Smin, D)]) for s in Signal]
    return S


def plot(Sign, x):
    Signal = Sign(x)
    Max = np.max(Signal)
    Min = np.min(Signal)
    Delta = delta(Max, Min)

    SignalFin = scalar_quantizer(Signal, Min, Delta)
    plt.plot(Signal)
    plt.plot(SignalFin)
    plt.show()


def plot_img(i):
    # open image
    image = Image.open(i)
    # transform img to signal
    Signal = image.getdata()
    # get size of img
    l, h = image.size

    # Quantizer algorithm
    Max = np.max(Signal)
    Min = np.min(Signal)
    Delta = delta(Max, Min)
    SignalFin = scalar_quantizer(Signal, Min, Delta)

    # create a new img
    res = Image.new("L", (l,h))
    # fill the img
    res.putdata(SignalFin)
    # save the file with his name
    res.save("new"+i)


def main():
    #test sin
    #plot(np.sin, np.linspace(-np.pi, np.pi, 201))
    plot_img('lena512.bmp')

main()

