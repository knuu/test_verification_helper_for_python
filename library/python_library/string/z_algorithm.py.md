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


# :heavy_check_mark: python_library/string/z_algorithm.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#a280567310207d0ec287bcfac252dc53">python_library/string</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library/string/z_algorithm.py">View this file on GitHub</a>
    - Last commit date: 2020-08-09 10:58:36+00:00




## Verified with

* :heavy_check_mark: <a href="../../../verify/tests/z_algorithm.test.py.html">tests/z_algorithm.test.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
def z_algorithm(S: str):
    ret = [0] * len(S)
    ret[0] = len(S)
    i, j = 1, 0
    while i < len(S):
        while i + j < len(S) and S[j] == S[i + j]:
            j += 1
        ret[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < len(S) and k + ret[k] < j:
            ret[i + k] = ret[k]
            k += 1
        i, j = i + k, j - k
    return ret

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

