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


# :heavy_check_mark: python_library/math/euler_totient.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#fcc812ea527936762e2a2536e11e6960">python_library/math</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library/math/euler_totient.py">View this file on GitHub</a>
    - Last commit date: 2020-08-09 10:27:47+00:00




## Verified with

* :heavy_check_mark: <a href="../../../verify/tests/euler_totient.test.py.html">tests/euler_totient.test.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
def euler_totient(n):
    if n <= 0:
        return 0
    ans = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            ans -= ans // i
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        ans -= ans // n
    return ans

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

