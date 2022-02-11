import numpy as np
import matplotlib.pyplot as plt


class Simulation:
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def run(self, start, simulations, iterations):
        # Create a list that repeats element `start`, `simulations` times.
        generation = [start] * simulations
        # Add it as the first result
        generations = [generation[:]]

        # For each iteration
        for _ in range(iterations):

            # Create normal distributed samples
            samples = np.random.normal(
                loc=self.mu, scale=self.sigma, size=simulations)

            # Update the current generation with the samples
            for index in range(simulations):
                generation[index] = generation[index] * samples[index]

            # Append **a copy** of the generation to the result.
            # `list[:]` makes a copy of `list`.
            generations.append(generation[:])

        # Return the generated generations
        return generations


simulation = Simulation(mu=1.00001, sigma=0.001)
simulations = simulation.run(start=1000, simulations=100, iterations=1000)
for s in simulations:
    print(s)

delta = 80
plt.ylim(1000-delta, 1000+delta)
plt.plot(simulations, scaley=False)
plt.show()
