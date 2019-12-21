from functools import reduce

from algs4.commonutils.random_utils import StdRandom
from .union_find import UnionFindCompressedWeightedQuickUnion


class Erdos:
    def __init__(self, N):
        self.N = N

    def run(self):
        uf = UnionFindCompressedWeightedQuickUnion(self.N)
        connections = 0
        while uf.component_count > 1:
            p = StdRandom.uniform_int(self.N)
            q = StdRandom.uniform_int(self.N)
            uf.union(p, q)
            connections += 1
        return connections


def main():
    import matplotlib.pyplot as plt
    arr = range(100, 10**5, 100)
    xs, ys = [], []
    for n in arr:
        erdos = Erdos(n)
        xs.append(n)
        ys.append(erdos.run())
        print("n:%d, connections: %d" % (xs[-1], ys[-1]))

    plt.scatter(xs, ys)
    plt.show(block=True)


if __name__ == "__main__":
    main()
