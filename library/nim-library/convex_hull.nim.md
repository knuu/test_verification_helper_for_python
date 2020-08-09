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


# :warning: nim-library/convex_hull.nim

<a href="../../index.html">Back to top page</a>

* category: <a href="../../index.html#dd390cd6b7c8b7d7cfc5543fc36ddaac">nim-library</a>
* <a href="{{ site.github.repository_url }}/blob/master/nim-library/convex_hull.nim">View this file on GitHub</a>
    - Last commit date: 2020-08-09 18:21:38+09:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
type
  Point[T] = object
    x, y: T

proc initPoint[T](x, y: T): Point[T] =
  Point[T](x: x, y: y)

proc `+`[T](a, b: Point[T]): Point[T] =
  initPoint(a.x + b.x, a.y + b.y)

proc `-`[T](a, b: Point[T]): Point[T] =
  initPoint(a.x - b.x, a.y - b.y)

proc det[T](a, b: Point[T]): T =
  a.x * b.y - a.y * b.x

proc convex_hull[T](points: seq[Point[T]]): seq[Point[T]] =
  var sorted_points = points
  sorted_points.sort do (p1, p2: Point[T]) -> int:
    result = cmp(p1.x, p2.x)
    if result == 0:
      result = cmp(p1.y, p2.y)
  var lower_hull = sorted_points.get_bounds
  sorted_points.reverse
  result = sorted_points.get_bounds
  discard lower_hull.pop
  discard result.pop
  for point in lower_hull:
    result.add(point)

proc get_bounds[T](points: var seq[Point[T]]): seq[Point[T]] =
  result = @[points[0], points[1]]
  for point in points[2..^1]:
    while result.len > 1 and (result[^1] - result[^2]).det(point - result[^1]) <= 0:
      discard result.pop
    result.add(point)

```
{% endraw %}

<a id="bundled"></a>
{% raw %}
```cpp
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.8.5/x64/lib/python3.8/site-packages/onlinejudge_verify/docs.py", line 349, in write_contents
    bundled_code = language.bundle(self.file_class.file_path, basedir=pathlib.Path.cwd())
  File "/opt/hostedtoolcache/Python/3.8.5/x64/lib/python3.8/site-packages/onlinejudge_verify/languages/nim.py", line 86, in bundle
    raise NotImplementedError
NotImplementedError

```
{% endraw %}

<a href="../../index.html">Back to top page</a>

