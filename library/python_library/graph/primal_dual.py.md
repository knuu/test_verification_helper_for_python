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


# :heavy_check_mark: python_library/graph/primal_dual.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#7e80885bc8a78dc63feed9f40126ba0e">python_library/graph</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library/graph/primal_dual.py">View this file on GitHub</a>
    - Last commit date: 2020-08-09 10:20:24+00:00




## Verified with

* :heavy_check_mark: <a href="../../../verify/tests/primal_dual.test.py.html">tests/primal_dual.test.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
import heapq


class MinCostFlow:
    class Edge:
        def __init__(self, to, cap, rev, cost):
            self.to, self.cap, self.rev, self.cost = to, cap, rev, cost

    def __init__(self, V):
        self.V = V
        self.E = [[] for _ in range(V)]

    def add_edge(self, fr, to, cap, cost):
        self.E[fr].append(self.Edge(to, cap, len(self.E[to]), cost))
        self.E[to].append(self.Edge(fr, 0, len(self.E[fr])-1, -cost))

    def run(self, source, sink, f, INF=10**5):
        res = 0
        h, prevv, preve = [0] * self.V, [0] * self.V, [0] * self.V
        while (f > 0):
            pque = []
            dist = [INF] * self.V
            dist[source] = 0
            heapq.heappush(pque, (0, source))
            while pque:
                cost, v = heapq.heappop(pque)
                cost = -cost
                if dist[v] < cost:
                    continue
                for i, e in enumerate(self.E[v]):
                    if e.cap > 0 and dist[v] - h[e.to] < dist[e.to] - e.cost - h[v]:
                        dist[e.to] = dist[v] + e.cost + h[v] - h[e.to]
                        prevv[e.to], preve[e.to] = v, i
                        heapq.heappush(pque, (-dist[e.to], e.to))
            if dist[sink] == INF:
                return -1
            for v in range(self.V):
                h[v] += dist[v]

            d, v = f, sink
            while v != source:
                d = min(d, self.E[prevv[v]][preve[v]].cap)
                v = prevv[v]
            f -= d
            res += d * h[sink]
            v = sink
            while v != source:
                self.E[prevv[v]][preve[v]].cap -= d
                self.E[v][self.E[prevv[v]][preve[v]].rev].cap += d
                v = prevv[v]
        return res

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

