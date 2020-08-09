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


# :warning: nim-library/heap.nim

<a href="../../index.html">Back to top page</a>

* category: <a href="../../index.html#dd390cd6b7c8b7d7cfc5543fc36ddaac">nim-library</a>
* <a href="{{ site.github.repository_url }}/blob/master/nim-library/heap.nim">View this file on GitHub</a>
    - Last commit date: 2020-08-09 18:21:38+09:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
type
  Heap[T]= object
    data: seq[T]
    size: int
    comp: proc (x: T, y: T): int
  EmptyHeapError = object of Exception

proc siftup[T](h: var Heap[T]) =
  var i = h.size - 1
  while i > 0:
    var par = (i-1) div 2
    if h.comp(h.data[par], h.data[i]) > 0:
      swap(h.data[i], h.data[par])
      i = par
    else:
      break
proc siftdown[T](h: var Heap[T]) =
  var par = 0
  while par < h.size:
    let (left, right) = (2*par+1, 2*par+2)
    if right < h.size:
      if h.comp(h.data[par], min(h.data[left], h.data[right])) <= 0:
        break
      elif h.comp(h.data[left], h.data[right]) < 0:
        swap(h.data[par], h.data[left])
        par = left
      else:
        swap(h.data[par], h.data[right])
        par = right
    elif left < h.size:
      if h.comp(h.data[left], h.data[par]) < 0:
        swap(h.data[par], h.data[left])
        par = left
      else:
        break
    else:
      break
proc initHeap[T](comparator: proc (x: T, y: T): int = cmp): Heap[T] =
  Heap[T](data: newSeq[T](), size: 0, comp: comparator)
proc push[T](h: var Heap[T], x: T) =
  h.data.add(x)
  h.size.inc
  h.siftup
proc pop[T](h: var Heap[T]): T =
  if h.size <= 0:
    raise newException(EmptyHeapError, "cannot pop element, heap is empty")
  result = h.data[0]
  h.data[0] = h.data[^1]
  h.size.dec
  h.data.setlen(h.size)
  h.siftdown
proc empty[T](h: var Heap[T]): bool {. inline .} = h.data.len == 0

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

