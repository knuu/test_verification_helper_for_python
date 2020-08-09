---
layout: default
---

<!-- mathjax config similar to math.stackexchange -->
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    TeX: { equationNumbers: { autoNumber: "AMS" }},
    tex2jax: {
      inlineMath: [ ['$','$'] ],
      processEscapes: true
    },
    "HTML-CSS": { matchFontHeight: false },
    displayAlign: "left",
    displayIndent: "2em"
  });
</script>

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery-balloon-js@1.1.2/jquery.balloon.min.js" integrity="sha256-ZEYs9VrgAeNuPvs15E39OsyOJaIkXEEt10fzxJ20+2I=" crossorigin="anonymous"></script>
<script type="text/javascript" src="../../../assets/js/copy-button.js"></script>
<link rel="stylesheet" href="../../../assets/css/copy-button.css" />


# :question: python_library/geometry/argument_sort.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#bb1189d107afaf50a8d799c22c656ecc">python_library/geometry</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library/geometry/argument_sort.py">View this file on GitHub</a>
    - Last commit date: 2020-08-09 10:20:24+00:00




## Verified with

* :heavy_check_mark: <a href="../../../verify/tests/argsort_yosupo1.test.py.html">tests/argsort_yosupo1.test.py</a>
* :x: <a href="../../../verify/tests/argsort_yosupo2.test.py.html">tests/argsort_yosupo2.test.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
import itertools
import sys
from functools import cmp_to_key
from typing import Iterable, List, Tuple


input = sys.stdin.buffer.readline


def argsort_numpy(points: List[Tuple[float, float]]
                  ) -> List[Tuple[float, float]]:
    import numpy as np
    args = [(np.arctan2(y, x, dtype=np.longdouble), idx)
            for idx, (x, y) in enumerate(points)]
    args.sort()
    return [points[i] for _, i in args]


def compare(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    if x1 * y2 == x2 * y1:
        return 0
    return 1 if x1 * y2 < x2 * y1 else -1


def argsort(points: List[Tuple[float, float]]
            ) -> Iterable[Tuple[float, float]]:
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


def yosupo():
    # https://judge.yosupo.jp/problem/sort_points_by_argument
    N = int(input())
    points = [tuple(int(val) for val in input().split()) for _ in range(N)]
    for x, y in argsort_numpy(points):
        print(x, y)


def yosupo2():
    # https://judge.yosupo.jp/problem/sort_points_by_argument
    N = int(input())
    points = [tuple(int(val) for val in input().split()) for _ in range(N)]
    for x, y in argsort(points):
        print(x, y)


if __name__ == "__main__":
    # yosupo()
    yosupo2()

```
{% endraw %}

<a id="bundled"></a>
{% raw %}
```cpp
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.8.5/x64/lib/python3.8/site-packages/onlinejudge_verify/docs.py", line 349, in write_contents
    bundled_code = language.bundle(self.file_class.file_path, basedir=pathlib.Path.cwd())
  File "/opt/hostedtoolcache/Python/3.8.5/x64/lib/python3.8/site-packages/onlinejudge_verify/languages/python.py", line 61, in bundle
    raise NotImplementedError
NotImplementedError

```
{% endraw %}

<a href="../../../index.html">Back to top page</a>

