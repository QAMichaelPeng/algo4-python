def three_sum_naive(ints):
    n = len(ints)
    ans = 0
    for i in range(n - 2):
        ai = ints[i]
        for j in range(i + 1, n - 1):
            aij = ai + ints[j]
            for k in range(j + 1, n):
                if aij + ints[k] == 0:
                    ans += 1
    return ans


def three_sum_fast(ints):
    n = len(ints)
    ints = sorted(ints)
    ans = 0
    for i in range(n - 2):
        ai = ints[i]
        target = -ai
        j, k = i + 1, n - 1
        while j < k:
            cur = ints[j] + ints[k]
            if cur == target:
                ans += 1
                j += 1
                k -= 1
            elif cur < target:
                j += 1
            else:
                k -= 1
    return ans


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser("Three sum")
    parser.add_argument("-i", dest="input_file")
    parser.add_argument("--algorithm", dest="algorithm")
    args = parser.parse_args()

    algorithm_map = {"naive": three_sum_naive, "fast": three_sum_fast}
    with open(args.input_file) as f:
        ints = [int(x) for x in f]
    ans = algorithm_map[args.algorithm](ints)
    print("%d" % ans)
