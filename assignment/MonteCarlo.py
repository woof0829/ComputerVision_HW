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
    angle = math.pi / 2 * np.random.random((steps,))
    for number in range(steps):
        if randomnumber[number] <= math.cos(angle[number]):
            counter += 1
            asix_x.append(angle[number])
            asix_y.append(randomnumber[number])
    figure = plt.plot(asix_x, asix_y)
    plt.show(figure)
    plt.title('MonteCarloIntegration')

if __name__ == '__main__':
    montecarlo(50100)
