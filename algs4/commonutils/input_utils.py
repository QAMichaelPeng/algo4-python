import sys


class StdIn:
    @staticmethod
    def read_all():
        return sys.stdin.read()

    @staticmethod
    def read_all_strings():
        return sys.stdin.read().split()

    @staticmethod
    def read_all_ints():
        return list(map(int, StdIn.read_all_strings()))

    @staticmethod
    def read_all_floats():
        return [float(s) for s in StdIn.read_all_strings()]


if __name__ == "__main__":
    sys.exit()

    print("Test StdIn.read_all()")
    s = StdIn.read_all()
    print("StdIn.read_all() result: %s" % s)

    print("Test StdIn.read_all_strings()")
    slist = StdIn.read_all_strings()
    print("StdIn.read_all_strings() result: %s" % slist)

    print("Test StdIn.read_all_floats()")
    flist = StdIn.read_all_floats()
    print("StdIn.read_all_floats() result: %s" % flist)

    print("Test StdIn.read_all_ints()")
    ilist = StdIn.read_all_ints()
    print("StdIn.read_all_ints() result: %s" % ilist)
