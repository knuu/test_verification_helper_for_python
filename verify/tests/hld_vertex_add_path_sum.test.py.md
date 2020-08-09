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
<script type="text/javascript" src="../../assets/js/copy-button.js"></script>
<link rel="stylesheet" href="../../assets/css/copy-button.css" />


# :heavy_check_mark: tests/hld_vertex_add_path_sum.test.py

<a href="../../index.html">Back to top page</a>

* category: <a href="../../index.html#b61a6d542f9036550ba9c401c80f00ef">tests</a>
* <a href="{{ site.github.repository_url }}/blob/master/tests/hld_vertex_add_path_sum.test.py">View this file on GitHub</a>
    - Last commit date: 2020-08-09 18:21:38+09:00


* see: <a href="https://judge.yosupo.jp/problem/vertex_add_path_sum">https://judge.yosupo.jp/problem/vertex_add_path_sum</a>


## Depends on

* :question: <a href="../../library/python_library/data_structures/segment_tree.py.html">python_library/data_structures/segment_tree.py</a>
* :question: <a href="../../library/python_library/graph/graph.py.html">python_library/graph/graph.py</a>
* :heavy_check_mark: <a href="../../library/python_library/graph/heavy_light_decomposition.py.html">python_library/graph/heavy_light_decomposition.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
# verify-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum
import operator
import sys
input = sys.stdin.buffer.readline

from python_library.data_structures.segment_tree import SegmentTree
from python_library.graph.graph import Graph
from python_library.graph.heavy_light_decomposition import HeavyLightDecomposition


def main() -> None:
    N, Q = map(int, input().split())
    weights = [int(x) for x in input().split()]
    graph = Graph(N)
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph.add_edge(u, v, 1)
        graph.add_edge(v, u, 1)
    hld = HeavyLightDecomposition(graph)
    new_weights = [0] * N
    for i in range(N):
        new_weights[hld.vid[i]] = weights[i]
    rsq = SegmentTree.create_from_array(new_weights, operator.add, 0)

    ans = []
    for _ in range(Q):
        t, a, b = map(int, input().split())
        if t == 0:
            rsq.update(hld.vid[a], rsq[hld.vid[a]] + b)
        else:
            ans.append(hld.query_path(a, b, 0, rsq.query, operator.add))
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()

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

<a href="../../index.html">Back to top page</a>

