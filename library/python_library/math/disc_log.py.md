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


# :heavy_check_mark: python_library/math/disc_log.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#fcc812ea527936762e2a2536e11e6960">python_library/math</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library/math/disc_log.py">View this file on GitHub</a>
    - Last commit date: 2020-08-09 11:23:01+00:00




## Verified with

* :heavy_check_mark: <a href="../../../verify/tests/disc_log.test.py.html">tests/disc_log.test.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
def solve_discrete_logarithm(g: int, y: int, m: int) -> int:
    """find x >= 0 s.t. g^x≡y (mod m) by baby-step giant-step
    """
    if m == 1:
        return 0
    if y == 1:
        return 0
    if g == 0 and y == 0:
        return 1

    sqrt_m = int(pow(m, 0.5) + 100)

    # Baby-step
    memo = {}
    baby = 1
    for b in range(sqrt_m):
        if baby == y:
            return b
        memo[baby * y % m] = b
        baby = baby * g % m

    # Giant-step
    giant = 1
    for a in range(1, sqrt_m + 3):
        giant = giant * baby % m
        b = memo.get(giant, -1)
        if b >= 0:
            x = a * sqrt_m - b
            return x if pow(g, x, m) == y else -1
    return -1

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

