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


# :heavy_check_mark: python_library/geometry/geometry.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#bb1189d107afaf50a8d799c22c656ecc">python_library/geometry</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library/geometry/geometry.py">View this file on GitHub</a>
    - Last commit date: 2020-08-09 13:18:46+00:00




## Required by

* :heavy_check_mark: <a href="convex_hull.py.html">python_library/geometry/convex_hull.py</a>


## Verified with

* :heavy_check_mark: <a href="../../../verify/tests/convex_hull.test.py.html">tests/convex_hull.test.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
def add(a, b, eps=1e-10):
    return 0 if abs(a + b) < eps * (abs(a) + abs(b)) else a + b


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, p):
        return Point(add(self.x, p.x), add(self.y, p.y))

    def __sub__(self, p):
        return Point(add(self.x, -p.x), add(self.y, -p.y))

    def __mul__(self, d):
        return Point(self.x * d, self.y * d)

    def __lt__(self, p):
        return (self.x, self.y) < (p.x, p.y)

    def dot(self, p):
        return add(self.x * p.x, self.y * p.y)

    def det(self, p):
        return add(self.x * p.y, -self.y * p.x)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

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

