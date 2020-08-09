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


# :heavy_check_mark: python_library/data_structures/weighted_unionfind.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#4f7277da04114aac533381a4614f94a3">python_library/data_structures</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library/data_structures/weighted_unionfind.py">View this file on GitHub</a>
    - Last commit date: 2020-08-09 13:03:09+00:00




## Verified with

* :heavy_check_mark: <a href="../../../verify/tests/weighted_unionfind.test.py.html">tests/weighted_unionfind.test.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
class WeightedUnionFindTree:
    """Disjoint-Set Data Structure with weight

    complexity:
        - init: O(n)
        - find, unite, same: O(alpha(n))
    """

    def __init__(self, n_nodes):
        self.par = [i for i in range(n_nodes)]  # parent
        self.rank = [0] * n_nodes  # depth of tree
        self.weights = [0] * n_nodes

    def find(self, x):
        if self.par[x] == x:
            return x
        root = self.find(self.par[x])
        self.weights[x] += self.weights[self.par[x]]
        self.par[x] = root
        return root

    def unite(self, x, y, weight=0):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            self.par[root_x] = root_y
            self.weights[root_x] = weight - self.weights[x] + self.weights[y]
        else:
            self.par[root_y] = root_x
            self.weights[root_y] = -weight - self.weights[y] + self.weights[x]
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        return self.weights[x] - self.weights[y]

```
{% endraw %}

<a id="bundled"></a>
{% raw %}
```cpp
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.8.5/x64/lib/python3.8/site-packages/onlinejudge_verify/docs.py", line 349, in write_contents
    bundled_code = language.bundle(self.file_class.file_path, basedir=pathlib.Path.cwd())
  File "/opt/hostedtoolcache/Python/3.8.5/x64/lib/python3.8/site-packages/onlinejudge_verify/languages/python.py", line 67, in bundle
    raise NotImplementedError
NotImplementedError

```
{% endraw %}

<a href="../../../index.html">Back to top page</a>

