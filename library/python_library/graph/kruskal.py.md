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


# :warning: python_library/graph/kruskal.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#7e80885bc8a78dc63feed9f40126ba0e">python_library/graph</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library/graph/kruskal.py">View this file on GitHub</a>
    - Last commit date: 2020-08-09 13:03:09+00:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
class MinimumSpanningTree:
    """ Kruskal's algorithm: find minimum spanning tree
        Complexity: O(E log(V))
        used in GRL2A(AOJ)
    """

    def __init__(self, V, E, start=0, INF=10**9):
        """ V: the number of vertexes
            E: adjacency list (undirected graph)
        """
        self.kruskal(V, E)

    def kruskal(self, V, E):
        edges = []
        for v1 in range(V):
            for v2, cost in E[v1]:
                if v1 < v2:
                    edges.append((cost, v1, v2))
        edges.sort(reverse=True)
        self.mincost = 0
        self.minSpanningTree = []
        uf = UnionFindTree(V)
        while len(self.minSpanningTree) < V-1:
            cost, v1, v2 = edges.pop()
            if uf.same(v1, v2) == False:
                self.mincost += cost
                uf.unite(v1, v2)
                self.minSpanningTree.append((v1, v2, cost))

    def minCost(self):
        return self.mincost

    def getMinSpanningTree(self):
        return sorted(self.minSpanningTree)

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

