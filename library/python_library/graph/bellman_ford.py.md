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


# :warning: python_library/graph/bellman_ford.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#7e80885bc8a78dc63feed9f40126ba0e">python_library/graph</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library/graph/bellman_ford.py">View this file on GitHub</a>
    - Last commit date: 2020-08-09 11:04:28+00:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
class BellmanFord:
    """Bellman-Ford algorithm : find the shortest path from a vertex
       Complexity: O(VE)
       used in GRL1A(AOJ)
    """

    def __init__(self, V, E, start, INF=10**9):
        """ V: the number of vertexes
            E: adjacency list
            start: start vertex
            INF: Infinity distance
        """
        self.V = V
        self.E = E
        self.bellman_ford(start, INF)

    def bellman_ford(self, start, INF):
        self.distance = [INF] * self.V  # distance from start
        self.prev = [-1] * self.V  # prev vertex of shortest path
        self.distance[start] = 0
        self.negativeCycle = False

        for i in range(self.V):
            update = False
            for fr in range(self.V):
                for to, cost in self.E[fr]:
                    if self.distance[fr] != INF and \
                       self.distance[fr] + cost < self.distance[to]:
                        self.distance[to] = self.distance[fr] + cost
                        self.prev[to] = fr
                        update = True
                        if i == self.V - 1:
                            self.negativeCycle = True
            if update:
                break

    def getPath(self, end):
        assert self.hasNegativeCycle() == False
        path = [end]
        while self.prev[end] != -1:
            end = self.prev[end]
        return path[::-1]

    def hasNegativeCycle(self):
        return self.negativeCycle

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

