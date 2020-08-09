# verify-helper: PROBLEM https://judge.yosupo.jp/problem/sort_points_by_argument
# verify-helper: IGNORE

import sys
from python_library.geometry.argument_sort import argsort_numpy

input = sys.stdin.buffer.readline


def main():
    N = int(input())
    points = [tuple(int(val) for val in input().split()) for _ in range(N)]
    for x, y in argsort_numpy(points):
        print(x, y)


if __name__ == "__main__":
    main()
