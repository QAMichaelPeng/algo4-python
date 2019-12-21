import random
from math import sqrt, log, ceil, exp


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
        return 1 if StdRandom.uniform() < p else 0

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

    @staticmethod
    def poisson(lam):
        exp_lam = exp(-lam)
        k = 0
        p = 1
        while p >= exp_lam:
            k += 1
            p *= StdRandom.uniform()
        return k - 1


def main():
    import matplotlib.pyplot as plt
    test_functions = []
    N = 1000000
    a = -5
    b = 23
    test_functions.append((lambda: StdRandom.uniform_range(a, b), "uniform(%s, %s)" % (a, b)))
    test_functions.append((lambda: StdRandom.uniform_int_range(a, b), "uniform_int(%d, %d)" % (a, b)))
    p = 0.8
    test_functions.append((lambda: StdRandom.bernoulli(p), "bernoulli(%s)" % p))
    mu = 33.3
    sigma = 44.4
    test_functions.append((lambda: StdRandom.gaussian(mu, sigma), "gaussian(%s, %s)" % (mu, sigma)))
    lam = 1
    test_functions.append((lambda: StdRandom.poisson(lam), "poisson(%s)" % lam))
    func_count = len(test_functions)
    w = ceil(sqrt(func_count))
    h = ceil(func_count / w)
    n_bins = 100
    fig, axs = plt.subplots(h, w, tight_layout=True)
    for i, (func, desc) in enumerate(test_functions):
        rfloats = [func() for _ in range(N)]
        y, x = i // w, i % w
        ax = axs[y][x]
        ax.hist(rfloats, bins=n_bins)
        ax.set_title(desc)

    plt.show(block=True)


if __name__ == "__main__":
    main()
