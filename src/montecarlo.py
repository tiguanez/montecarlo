import numpy as np
import matplotlib.pyplot as plt


class Simulation:
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def run(self, start, simulations, iterations):
        # Create an list that repeats element `start`, `simulations` times.
        generation = [start] * simulations
        # Add it as the first result
        generations = [generation[:]]

        # For each iteration
        for _ in range(iterations):

            # For each simulation
            for index in range(simulations):
                # Take a normal distributed sample
                sample = np.random.normal(loc=self.mu, scale=self.sigma)
                # Update the current generation with the sample
                generation[index] = generation[index] * sample

            # Append **a copy** of the generation to the result.
            # `list[:]` makes a copy of `list`.
            generations.append(generation[:])

        # Return the generated generations
        return generations


simulation = Simulation(mu=1.00001, sigma=0.001)
simulations = simulation.run(start=1000, simulations=10, iterations=100)
for s in simulations:
    print(s)

delta = 50
plt.ylim(1000-delta, 1000+delta)
plt.plot(simulations, scaley=False)
plt.show()
