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


# :x: python_library/data_structures/range_tree_2d.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#4f7277da04114aac533381a4614f94a3">python_library/data_structures</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library/data_structures/range_tree_2d.py">View this file on GitHub</a>
    - Last commit date: 2020-08-09 10:02:04+00:00




## Verified with

* :x: <a href="../../../verify/tests/range_tree_2d.test.py.html">tests/range_tree_2d.test.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
import bisect
from typing import List, Tuple


RangeType = Tuple[int, int]


class RangeTreeNode:
    def __init__(self, inf=10 ** 10):
        self._inf = inf
        self.range_ = (inf, inf)
        self.indices = []
        self.assoc = []

    @classmethod
    def merge(cls, node1: "RangeTreeNode", node2: "RangeTreeNode", data):
        merged_node = cls()
        merged_node.range_ = (
            min(node1.range_[0], node2.range_[0]),
            max(node1.range_[1], node2.range_[1]),
        )
        sentinel = node1._inf
        node1.assoc.append(sentinel)
        node2.assoc.append(sentinel)
        i = j = 0
        while min(node1.assoc[i], node2.assoc[j]) < sentinel:
            if node1.assoc[i] < node2.assoc[j] or (
                node1.assoc[i] == node2.assoc[j]
                and data[node1.indices[i]][0] < data[node2.indices[j]][0]
            ):
                merged_node.assoc.append(node1.assoc[i])
                merged_node.indices.append(node1.indices[i])
                i += 1
            else:
                merged_node.assoc.append(node2.assoc[j])
                merged_node.indices.append(node2.indices[j])
                j += 1
        node1.assoc.pop()
        node2.assoc.pop()
        return merged_node


class RangeTree2D:
    def __init__(self, inf=10 ** 10):
        self._inf = inf

    def build(self, points_: List[Tuple[int, int]]) -> None:
        points = sorted([(x, y, i) for i, (x, y) in enumerate(points_)])
        self._size = 1
        while self._size < len(points):
            self._size <<= 1
        self._data = [RangeTreeNode() for _ in range(self._size * 2 - 1)]
        for i, (x, y, idx) in enumerate(points):
            self._data[self._size - 1 + i].range_ = (x, x)
            self._data[self._size - 1 + i].indices.append(idx)
            self._data[self._size - 1 + i].assoc.append(y)
        for i in reversed(range(self._size - 1)):
            self._data[i] = RangeTreeNode.merge(
                self._data[2 * i + 1], self._data[2 * i + 2], points
            )

    def query(
        self, range_x: RangeType, range_y: RangeType, output: List[int], idx: int = 0
    ) -> None:
        if idx >= 2 * self._size - 1:
            return
        elif (
            range_x[0] <= self._data[idx].range_[0]
            and self._data[idx].range_[1] <= range_x[1]
        ):
            low = bisect.bisect_left(self._data[idx].assoc, range_y[0])
            high = bisect.bisect_left(self._data[idx].assoc, range_y[1] + 1)

            for i in range(low, high):
                output.append(self._data[idx].indices[i])
            return
        else:
            self.query(range_x, range_y, output, 2 * idx + 1)
            self.query(range_x, range_y, output, 2 * idx + 2)

    def count(self, range_x, range_y, idx=0):
        if idx >= 2 * self._size - 1:
            return 0
        elif (
            range_x[0] <= self._data[idx].range_[0]
            and self._data[idx].range_[1] <= range_x[1]
        ):
            low = bisect.bisect_left(self._data[idx].assoc, range_y[0])
            high = bisect.bisect_left(self._data[idx].assoc, range_y[1] + 1)
            return high - low
        else:
            return self.count(range_x, range_y, 2 * idx + 1) + self.count(
                range_x, range_y, 2 * idx + 2
            )

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

