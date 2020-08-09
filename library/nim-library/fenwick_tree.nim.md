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


# :warning: nim-library/fenwick_tree.nim

<a href="../../index.html">Back to top page</a>

* category: <a href="../../index.html#dd390cd6b7c8b7d7cfc5543fc36ddaac">nim-library</a>
* <a href="{{ site.github.repository_url }}/blob/master/nim-library/fenwick_tree.nim">View this file on GitHub</a>
    - Last commit date: 2020-08-09 18:21:38+09:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
import sequtils

type
  FenwickTree[T] = object
    dat: seq[T]
    size: Natural
    initial: T

proc initFenwickTree[T](size: Natural, initial: T): FenwickTree[T] =
  return FenwickTree[T](dat: newSeqWith(size, initial), size: size, initial: initial)

proc update[T](fwt: var FenwickTree[T], k: Natural, val: T) =
  assert(k < fwt.size)
  var key = k
  while key < fwt.size:
    fwt.dat[key] += val
    key = key or (key + 1)

proc query[T](fwt: var FenwickTree[T], k: int): T =
  assert(k >= 0)
  var key = k - 1
  result = fwt.initial
  while key >= 0:
    result += fwt.dat[key]
    key = (key and (key + 1)) - 1

proc query[T](fwt: var FenwickTree[T], left, right: Natural): T =
  assert(left <= right and right <= fwt.size)
  return fwt.query(right) - fwt.query(left)

proc index[T](fwt: var FenwickTree[T], k: Natural): T =
  assert(k < fwt.size)
  return fwt.query(k + 1) - fwt.index(k)

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

