import random
from math import sqrt, log


class StdRandom:
    @staticmethod
    def set_seed(seed=None):
        random.seed(seed)

    @staticmethod
    def uniform():
        """
        Generate a float number in [0.0, 1.0)

        :return: a float number in [0.0, 1.0)
        """
        return random.random()

    @staticmethod
    def uniform_int(n):
        """
        Generate an int number in [0, n)

        :return: an int number in [0, n)
        """
        return random.randrange(n)

    @staticmethod
    def uniform_int_range(a: int, b: int) -> int:
        """
        Generate an int number in [a, b)

        :return: an int number in [a, b)
        """
        return random.randrange(a, b)

    @staticmethod
    def uniform_range(a: float, b: float) -> float:
        """
        Generate an float number in [a, b)

        :return: an float number in [a, b)
        """
        return random.uniform(a, b)

    @staticmethod
    def bernoulli(p: float = 0.5):
        return StdRandom.uniform() < p

    @staticmethod
    def gaussian(mu=0, sigma=1):
        # Box Muller algorithm
        while True:
            x = StdRandom.uniform_range(-1, 1)
            y = StdRandom.uniform_range(-1, 1)
            r2 = x * x + y * y
            if 0 < r2 < 1:
                break
        return x * sqrt(-2 * log(1 - r2) / r2) * sigma + mu


def main():
    import pandas
    import matplotlib.pyplot as plt
    N = 10000
    rfloats = [StdRandom.uniform() for _ in range(N)]
    rseries = pandas.Series(rfloats)
    print("describe uniform() %d: %s" % (N, rseries.describe()))
    n = 100
    rints = [StdRandom.uniform_int(100) for _ in range(N)]
    rseries = pandas.Series(rints)
    print("describe: uniform(%d), %d: %s" % (n, N, rseries.describe()))
    a, b = 20, 1200
    rints = [StdRandom.uniform_int_range(a, b) for _ in range(N)]
    rseries = pandas.Series(rints)
    print("describe: uniform_int_range(%d, %d), %d: %s" % (a, b, N, rseries.describe()))

    a, b = 20.8, 1200.3
    rfloats = [StdRandom.uniform_range(a, b) for _ in range(N)]
    rseries = pandas.Series(rfloats)
    print("describe: uniform_range(%s, %s), %d: %s" % (a, b, n, rseries.describe()))

    p = 0.8
    avg = sum([StdRandom.bernoulli(p) for _ in range(N)]) / N
    print("bernoulli %s avg: %s" % (p, avg))

    mu = 3.4
    sigma = 2.8
    rfloats = [StdRandom.gaussian(mu, sigma) for _ in range(N)]
    rseries = pandas.Series(rfloats)
    print("describe: gaussian(%s, %s), %s" % (mu, sigma, rseries.describe()))
    n_bins = 20
    fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
    axs[0].hist(rfloats, bins=n_bins)
    plt.show()


if __name__ == "__main__":
    main()
