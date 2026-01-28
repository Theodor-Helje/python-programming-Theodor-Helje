import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

rng = np.random.default_rng()

random = rng.integers(100, size=100)
uniform = rng.uniform(size=100)
normal = rng.normal(size=100)
binominal = rng.binomial(n=10, p=.3, size=100)
negative_binominal = rng.negative_binomial(n=10, p=.3, size=100)
gamma = rng.gamma(shape=1.0, scale=0.9, size=100)
geometric = rng.geometric(p=0.31, size=100)
distributions = [
    random, uniform, normal, binominal, negative_binominal, gamma, geometric
    ]
distribution_names = [
    'random', 'uniform', 'normal', 'binominal', 'nagative binominal', 'gamma', 'geometric'
]


def run_game():
    score = 0
    while True:
        plot_index = np.random.randint(len(distributions))
        plot = distributions[plot_index]

        if np.random.choice([True, False]):
            sns.histplot(data=plot, bins=50)
            plt.title("Guess the distribution!")
        else:
            sns.lineplot(x=np.sort(plot), y=np.arange(1, len(plot) + 1))
            plt.title("Guess the ogive!")

        print("options:")
        #print("enter to exit game")
        for i, _ in enumerate(distributions):
            print(f"{i+1}: {distribution_names[i]}")
        
        plt.show()

        if int(input()) == plot_index + 1:
            print(f"Correct, it was {distribution_names[plot_index]}")
            score += 1
        else:
            print(f"No, it was {distribution_names[plot_index]}")
        
        input(f"Score: {score}")

random = rng.integers(100, size=100)
uniform = rng.uniform(size=100)
normal = rng.normal(size=100)
binominal = rng.binomial(n=10, p=.3, size=100)
negative_binominal = rng.negative_binomial(n=10, p=.3, size=100)
gamma = rng.gamma(shape=1.0, scale=0.9, size=100)
geometric = rng.geometric(p=0.31, size=100)
distributions = [
    random, uniform, normal, binominal, negative_binominal, gamma, geometric
    ]
distribution_names = [
    'random', 'uniform', 'normal', 'binominal', 'nagative binominal', 'gamma', 'geometric'
]


fig, axes = plt.subplots(2, 4, figsize=(15, 7))
axes = axes.ravel()

for data, ax, title in zip(distributions, axes, distribution_names):
    sns.histplot(data=data, ax=ax, bins=50)
    ax.set_title(title)

plt.show()


fig, axes = plt.subplots(2, 4, figsize=(15, 7))
axes = axes.ravel()

for data, ax, title in zip(distributions, axes, distribution_names):
    sns.lineplot(x=np.sort(data), y=np.arange(1, len(data) + 1), ax=ax)
    ax.set_title(title)

plt.show()

print("Done, entering game")

run_game()