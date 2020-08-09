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


# :warning: python_library/math/givens.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#fcc812ea527936762e2a2536e11e6960">python_library/math</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library/math/givens.py">View this file on GitHub</a>
    - Last commit date: 2020-08-09 11:23:01+00:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
def givens(A, b):
    """ solve linear equation
        cf. http://www.slideshare.net/tmaehara/ss-18244588
        complexity: O(n^3)
        used in kupc2012_C
    """
    def mkrot(x, y):
        r = pow(x**2+y**2, 0.5)
        return x/r, y/r

    def rot(x, y, c, s):
        return c*x+s*y, -s*x+c*y

    n = len(b)
    for i in range(n):
        for j in range(i+1, n):
            c, s = mkrot(A[i][i], A[j][i])
            b[i], b[j] = rot(b[i], b[j], c, s)
            for k in range(i, n):
                A[i][k], A[j][k] = rot(A[i][k], A[j][k], c, s)
    for i in reversed(range(n)):
        for j in range(i+1, n):
            b[i] -= A[i][j] * b[j]
        b[i] /= A[i][i]
    return b

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

