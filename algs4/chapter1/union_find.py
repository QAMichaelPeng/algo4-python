class UnionFindQuickUnion:
    def __init__(self, N):
        self.parents = list(range(N))
        self.access_count = 0
        self.component_count = N
        self.costs = []
        self.average_costs = []

    def find(self, p):
        while p != self.parents[p]:
            p = self.parents[p]
            self.access_count += 2
        self.access_count += 1
        return p

    def union(self, p, q):
        old = self.access_count
        p = self.find(p)
        q = self.find(q)
        if p == q:
            self.costs.append(self.access_count - old)
            self.average_costs.append(self.access_count / len(self.costs))
            return
        self.parents[p] = q
        self.access_count += 1
        self.component_count -= 1
        self.costs.append(self.access_count - old)
        self.average_costs.append(self.access_count / len(self.costs))

    def roots(self):
        ans = []
        for i in range(len(self.parents)):
            if self.parents[i] == i:
                ans.append(i)
        return ans


class UnionFindCompressedQuickUnion:
    def __init__(self, N):
        self.parents = list(range(N))
        self.access_count = 0
        self.component_count = N
        self.costs = []
        self.average_costs = []

    def find(self, p):
        parent = self.parents[p]
        if p == parent:
            self.access_count += 1
            return p
        parent = self.find(parent)
        self.parents[p] = parent
        self.access_count += 2
        return parent

    def union(self, p, q):
        old = self.access_count
        p = self.find(p)
        q = self.find(q)
        if p == q:
            self.costs.append(self.access_count - old)
            self.average_costs.append(self.access_count / len(self.costs))
            return
        self.parents[p] = q
        self.access_count += 1
        self.component_count -= 1
        self.costs.append(self.access_count - old)
        self.average_costs.append(self.access_count / len(self.costs))

    def roots(self):
        ans = []
        for i in range(len(self.parents)):
            if self.parents[i] == i:
                ans.append(i)
        return ans


class UnionFindWeightedQuickUnion:
    def __init__(self, N):
        self.parents = list(range(N))
        self.weights = [1] * N
        self.access_count = 0
        self.component_count = N
        self.costs = []
        self.average_costs = []

    def find(self, p):
        while p != self.parents[p]:
            p = self.parents[p]
            self.access_count += 2
        self.access_count += 1
        return p

    def union(self, p, q):
        old = self.access_count
        p = self.find(p)
        q = self.find(q)
        if p == q:
            self.costs.append(self.access_count - old)
            self.average_costs.append(self.access_count / len(self.costs))
            return
        if self.weights[p] > self.weights[q]:
            p, q = q, p
        self.parents[p] = q
        self.weights[q] += self.weights[p]
        self.access_count += 1
        self.component_count -= 1
        self.costs.append(self.access_count - old)
        self.average_costs.append(self.access_count / len(self.costs))

    def roots(self):
        ans = []
        for i in range(len(self.parents)):
            if self.parents[i] == i:
                ans.append(i)
        return ans


class UnionFindCompressedWeightedQuickUnion:
    def __init__(self, N):
        self.parents = list(range(N))
        self.weights = [1] * N
        self.access_count = 0
        self.component_count = N
        self.costs = []
        self.average_costs = []

    def find(self, p):
        parent = self.parents[p]
        if p == parent:
            self.access_count += 1
            return p
        parent = self.find(parent)
        self.parents[p] = parent
        self.access_count += 2
        return parent

    def union(self, p, q):
        old = self.access_count
        p = self.find(p)
        q = self.find(q)
        if p == q:
            self.costs.append(self.access_count - old)
            self.average_costs.append(self.access_count / len(self.costs))
            return
        if self.weights[p] > self.weights[q]:
            p, q = q, p
        self.parents[p] = q
        self.weights[q] += self.weights[p]
        self.access_count += 1
        self.component_count -= 1
        self.costs.append(self.access_count - old)
        self.average_costs.append(self.access_count / len(self.costs))

    def roots(self):
        ans = []
        for i in range(len(self.parents)):
            if self.parents[i] == i:
                ans.append(i)
        return ans


class UnionFindHeightedQuickUnion:
    def __init__(self, N):
        self.parents = list(range(N))
        self.heights = [1] * N
        self.access_count = 0
        self.component_count = N
        self.costs = []
        self.average_costs = []

    def find(self, p):
        while p != self.parents[p]:
            p = self.parents[p]
            self.access_count += 2
        self.access_count += 1
        return p

    def union(self, p, q):
        old = self.access_count
        p = self.find(p)
        q = self.find(q)
        if p == q:
            self.costs.append(self.access_count - old)
            self.average_costs.append(self.access_count / len(self.costs))
            return
        if self.heights[p] > self.heights[q]:
            p, q = q, p
        self.parents[p] = q
        self.heights[q] = max(self.heights[q], self.heights[p] + 1)
        self.access_count += 1
        self.component_count -= 1
        self.costs.append(self.access_count - old)
        self.average_costs.append(self.access_count / len(self.costs))

    def roots(self):
        ans = []
        for i in range(len(self.parents)):
            if self.parents[i] == i:
                ans.append(i)
        return ans


class UnionFindQuickFind:
    def __init__(self, N):
        self.parents = list(range(N))
        self.access_count = 0
        self.component_count = N
        self.costs = []
        self.average_costs = []

    def find(self, p):
        while p != self.parents[p]:
            p = self.parents[p]
            self.access_count += 2
        self.access_count += 1
        return p

    def union(self, p, q):
        old = self.access_count
        p = self.find(p)
        q = self.find(q)
        if p == q:
            self.costs.append(self.access_count - old)
            self.average_costs.append(self.access_count / len(self.costs))
            return
        for i, x in enumerate(self.parents):
            if x == p:
                self.parents[i] = q
                self.access_count += 1

        self.access_count += len(self.parents)
        self.component_count -= 1
        self.costs.append(self.access_count - old)
        self.average_costs.append(self.access_count / len(self.costs))

    def roots(self):
        ans = []
        for i in range(len(self.parents)):
            if self.parents[i] == i:
                ans.append(i)
        return ans


if __name__ == "__main__":
    import argparse
    import matplotlib.pyplot as plt

    parser = argparse.ArgumentParser("Union Find")
    parser.add_argument("-i", dest="input_file")
    parser.add_argument("--algorithm", dest="algorithm")
    args = parser.parse_args()

    algorithm_map = {"quickunion": UnionFindQuickUnion, "quickfind": UnionFindQuickFind,
                     "weightedquickunion": UnionFindWeightedQuickUnion,
                     "heightedquickunion": UnionFindHeightedQuickUnion,
                     "compressedquickunion": UnionFindCompressedQuickUnion,
                     "compressedweightedquickunion": UnionFindCompressedWeightedQuickUnion,
                     }
    with open(args.input_file) as f:
        n = int(f.readline())
        print("%d dots" % n)
        uf = algorithm_map[args.algorithm](n)
        for line in f:
            x, y = map(int, line.split())
            uf.union(x, y)
        print("%d connected components" % uf.component_count)
        plt.scatter(range(1, 1 + len(uf.costs)), uf.costs, c="0.75", marker=".")
        plt.scatter(range(1, 1 + len(uf.costs)), uf.average_costs, c="red", marker=".")
        plt.show(block=True)
