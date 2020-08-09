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


# :warning: python_library/graph/graph2.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#7e80885bc8a78dc63feed9f40126ba0e">python_library/graph</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library/graph/graph2.py">View this file on GitHub</a>
    - Last commit date: 2020-08-09 12:53:27+00:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
class Edge:
    def __init__(self, src, dst):
        self.src, self.dst = src, dst


class WeightedEdge(Edge):
    def __init__(self, src, dst, weight):
        self.src, self.dst, self.weight = src, dst, weight


class ResidualEdge(Edge):
    def __init__(self, src, dst, cap):
        self.src, self.dst, self.cap = src, dst, cap

    def reverse(self):
        return ResidualEdge(self.dst, self.src, 0)


class Graph:
    def __init__(self, n, EdgeClass):
        pass

    def add_edge(self, *args):
        pass

    def add_undirected_edge(self, *args):
        pass


class AdjacencyList(Graph):
    def __init__(self, n, EdgeClass):
        self._graph = [[] for _ in range(n)]
        self.EdgeClass = EdgeClass

    def add_edge(self, *args):
        edge = self.EdgeClass(*args)
        self._graph[edge.src].append(edge)

    def add_undirected_edge(self, *args):
        edge = self.EdgeClass(*args)
        self._graph[edge.src].append(edge)
        edge.src, edge.dst = edge.dst, edge.src
        self._graph[edge.src].append(edge)

    def __getitem__(self, key):
        return self._graph[key]


class ResidualGraph(AdjacencyList):
    def __init__(self, n):
        super().__init__(n, ResidualEdge)

    def add_edge(self, *args):
        edge = self.EdgeClass(*args)
        edge.rev = len(self._graph[edge.dst])
        self._graph[edge.src].append(edge)
        rev = edge.reverse()
        rev.rev = len(self._graph[rev.dst]) - 1
        self._graph[edge.src].append(rev)

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

