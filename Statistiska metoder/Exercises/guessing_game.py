import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
        print("enter to exit game")
        for i, _ in enumerate(distributions):
            print(f"{i+1}: {distribution_names[i]}")
        
        plt.show()


        guess = input()

        try:
            guess = int(guess)
        except ValueError:
            print(f"score: {score}")
            return
        
        if guess == plot_index + 1:
            print(f"Correct, it was {distribution_names[plot_index]}")
            score += 1
        else:
            print(f"No, it was {distribution_names[plot_index]}")
        
        input(f"Score: {score}")

if __name__ == '__main__':
    print("running game...")
    run_game()