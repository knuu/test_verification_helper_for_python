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


# :warning: python_library/math/combinations.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#fcc812ea527936762e2a2536e11e6960">python_library/math</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library/math/combinations.py">View this file on GitHub</a>
    - Last commit date: 2020-08-09 10:58:36+00:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
mod = 10**9+7


def inv(x):
    return pow(x, mod - 2, mod)


def nCk(n, k):
    assert 0 <= k <= n
    k = min(k, n - k)
    ret = 1
    for i in range(k):
        ret *= n - i
        ret %= mod
        ret *= inv(i + 1)
        ret %= mod
    return ret


def nHk(n, k):
    assert 1 <= k <= n
    return nCk(n + k - 1, k - 1)

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

