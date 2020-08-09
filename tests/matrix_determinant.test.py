# verify-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_det
import sys
input = sys.stdin.buffer.readline

from python_library.data_structures.matrix import Matrix, det


def main() -> None:
    N = int(input())
    mat = [[int(x) for x in input().split()] for _ in range(N)]
    print(det(Matrix(mat)))


if __name__ == "__main__":
    main()
