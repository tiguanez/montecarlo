import numpy as np
import matplotlib.pyplot as plt

class Iteration:
    def __init__(self, count, mu, sigma):
        self.count = count
        self.mu = mu
        self.sigma = sigma

    def run(self, start):
        generation = start
        result = []
        for x in range(self.count):
            result.append(generation)
            generation = generation * \
                np.random.normal(loc=self.mu, scale=self.sigma)
        return result


def run_simulations(simulations):
    result = []
    for x in range(simulations):
        iteration = Iteration(10, 1, 0.001)
        result.append(iteration.run(1000))
    return result


simulations = run_simulations(10)
print(simulations[0])
plt.plot(simulations[0])
plt.show()
