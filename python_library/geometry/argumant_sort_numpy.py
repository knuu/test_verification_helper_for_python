from typing import List, Tuple


def argsort_numpy(points: List[Tuple[float, float]]
                  ) -> List[Tuple[float, float]]:
    import numpy as np
    args = [(np.arctan2(y, x, dtype=np.longdouble), idx)
            for idx, (x, y) in enumerate(points)]
    args.sort()
    return [points[i] for _, i in args]
