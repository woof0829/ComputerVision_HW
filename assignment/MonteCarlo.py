# MonteCarlo
import math
import numpy as np
import matplotlib.pyplot as plt


def montecarlo(steps):
    counter = 0
    # counter initialization
    asix_x = []
    asix_y = []
    # initialize a list to store asix value
    randomnumber = np.random.random((steps,))
    angle = math.pi / 2 * randomnumber
    for number in range(steps):
        if randomnumber[number] <= math.cos(angle[number]):
            counter += 1
            asix1 = angle[number]
            asix_x[counter] = asix1
            asix2 = randomnumber[number]
            asix_y[counter] = asix2
    region = math.pi / 2 * counter * steps
    figure = plt.plot(asix_x, asix_y)
    plt.show(figure)
    print region


if __name__ == '__main__':
    montecarlo(2)
