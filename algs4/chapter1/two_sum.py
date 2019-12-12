def two_sum_naive(ints):
    n = len(ints)
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if ints[i] + ints[j] == 0:
                ans += 1
    return ans


def two_sum_fast(ints):
    ints = sorted(ints)
    n = len(ints)
    ans = 0
    for i in range(n - 1):
        a = ints[i]
        j = bisect.bisect_left(ints, -a, i)
        if j < n and ints[j] + a == 0:
            ans += 1
    return ans


def two_sum_faster(ints):
    ints = sorted(ints)
    n = len(ints)
    ans = 0
    i, j = 0, n - 1
    while i < j:
        cur = ints[i] + ints[j]
        if cur == 0:
            ans += 1
            i += 1
            j -= 1
        elif cur < 0:
            i += 1
        else:
            j -= 1
    return ans


if __name__ == "__main__":
    import argparse
    import bisect

    parser = argparse.ArgumentParser("Two sum")
    parser.add_argument("-i", dest="input_file")
    parser.add_argument("--algorithm", dest="algorithm")
    args = parser.parse_args()

    algorithm_map = {"naive": two_sum_naive, "fast": two_sum_fast, "faster": two_sum_faster}
    with open(args.input_file) as f:
        ints = [int(x) for x in f]
    ans = algorithm_map[args.algorithm](ints)
    print("%d" % ans)
