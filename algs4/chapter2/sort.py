from stopwatch import Stopwatch

from algs4.commonutils.random_utils import StdRandom


class Selection:
    @staticmethod
    def sort(l):
        n = len(l)
        for i in range(n):
            mini = i
            min_value = l[mini]
            for j in range(i + 1, n):
                if l[j] < min_value:
                    mini = j
                    min_value = l[j]
            l[i], l[mini] = l[mini], l[i]


class Insertion:
    @staticmethod
    def sort(l):
        n = len(l)
        exch = 0
        for i in range(n):
            j = i - 1
            saved = l[i]
            while j >= 0:
                cur = l[j]
                if cur > saved:
                    l[j + 1] = cur
                    exch += 1
                    j -= 1
                else:
                    break
            l[j + 1] = saved


class InsertionSentinel:
    @staticmethod
    def sort(l):
        n = len(l)
        if n == 0:
            return
        mini = 0
        minv = l[0]
        for i, v in enumerate(l):
            if v < minv:
                minv = v
                mini = i
        if mini != 0:
            l[0], l[mini] = l[mini], l[0]
        for i in range(1, n):
            j = i - 1
            saved = l[i]
            while l[j] > saved:
                l[j + 1] = l[j]
                j -= 1
            if j + 1 < i:
                l[j + 1] = saved


class ShellSort:
    @staticmethod
    def sort(l):
        n = len(l)
        h = 1
        exch = 0
        factor = 3
        while h < n // factor:
            h = factor * h + 1
        while h >= 1:
            print("h: %d" % h)
            for i in range(h, n, 1):
                j = i - h
                saved = l[i]
                while j >= 0 and l[j] > saved:
                    l[j + h] = l[j]
                    exch += 1
                    j -= h
                if j + h != i:
                    l[j + h] = saved
            h //= factor
        print("Shell sort %d exch %d times" % (n, exch))


def is_sort(arr):
    for i in range(len(arr) - 1):
        assert arr[i] <= arr[i + 1]


def main(sort_klass, T):
    arr = [0] * T
    for i in range(T):
        arr[i] = StdRandom.uniform()

    sorted_arr = sorted(arr)
    stopwatch = Stopwatch()
    sort_klass.sort(arr)
    print("Take time %s" % stopwatch.duration)
    is_sort(arr)
    assert sorted_arr == arr


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser("Union Find")
    parser.add_argument("--algorithm", dest="algorithm")
    parser.add_argument("-s", dest="input_size", type=int)
    args = parser.parse_args()

    algorithm_map = {"selection": Selection, "insertion": Insertion, "shell": ShellSort,
                     "insertionsentinel": InsertionSentinel}
    main(algorithm_map[args.algorithm], args.input_size)
