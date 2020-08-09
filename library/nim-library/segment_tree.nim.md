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


# :warning: nim-library/segment_tree.nim

<a href="../../index.html">Back to top page</a>

* category: <a href="../../index.html#dd390cd6b7c8b7d7cfc5543fc36ddaac">nim-library</a>
* <a href="{{ site.github.repository_url }}/blob/master/nim-library/segment_tree.nim">View this file on GitHub</a>
    - Last commit date: 2020-08-09 18:21:38+09:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
type
  SegTree[T] = object
    dat: seq[T]
    size: Natural
    real_size: Natural
    merge: proc (x, y: T): T
    default: T

proc max_merge[T](x, y: T): T =
  result = if x > y: x else: y

proc min_merge[T](x, y: T): T =
  result = if x > y: y else: x

proc sum_merge[T](x, y: T): T = x + y

proc initSegTree[T](size: Natural, merge: proc (x, y: T): T = max_merge, default = 0): SegTree[T] =
  var real_size = 1
  while real_size < size: real_size = real_size shl 1
  return SegTree[T](
    dat: newSeqWith(2 * real_size - 1, default),
    size: size,
    real_size: real_size,
    merge: merge,
    default: default
  )

proc update[T](segt: var Segtree[T], k: Natural, val: T) =
  assert(k < segt.size)
  var key = k + segt.real_size - 1
  segt.dat[key] = val
  while key > 0:
    key = (key - 1) div 2
    segt.dat[key] = segt.merge(segt.dat[2 * key + 1], segt.dat[2 * key + 2])

proc query[T](segt: var SegTree[T], a, b, k, left, right: Natural): T =
  if right <= a or b <= left: return segt.default
  if a <= left and right <= b: return segt.dat[k]
  let mid = (left + right) div 2
  return segt.merge(segt.query(a, b, 2 * k + 1, left, mid),
                   segt.query(a, b, 2 * k + 2, mid, right))

proc query[T](segt: var SegTree[T], a, b: Natural): T =
  return segt.query(a, b, 0, 0, segt.real_size)

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

