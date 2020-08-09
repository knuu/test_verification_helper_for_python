import itertools
from functools import cmp_to_key
from typing import Iterable, List, Tuple


def compare(p1, p2) -> int:
    (x1, y1), (x2, y2) = p1, p2
    if x1 * y2 == x2 * y1:
        return 0
    return 1 if x1 * y2 < x2 * y1 else -1


def argsort(points: List[Tuple[float, float]]
            ) -> Iterable[Tuple[float, float]]:
    # argsort without numpy
    lowers, uppers, origins = [], [], []

    for x, y in points:
        if y < 0 or (y == 0 and x > 0):
            lowers.append((x, y))
        elif y > 0 or (y == 0 and x < 0):
            uppers.append((x, y))
        else:
            origins.append((x, y))
    lowers.sort(key=cmp_to_key(compare))
    uppers.sort(key=cmp_to_key(compare))
    origins.sort(key=cmp_to_key(compare))
    return itertools.chain(lowers, origins, uppers)
