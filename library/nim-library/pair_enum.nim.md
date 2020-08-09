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


# :warning: nim-library/pair_enum.nim

<a href="../../index.html">Back to top page</a>

* category: <a href="../../index.html#dd390cd6b7c8b7d7cfc5543fc36ddaac">nim-library</a>
* <a href="{{ site.github.repository_url }}/blob/master/nim-library/pair_enum.nim">View this file on GitHub</a>
    - Last commit date: 2020-08-09 18:21:38+09:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
# import sequtils, strutils, strscans, algorithm, math, future, sets, queues, tables # for yukicoder (0.17.1)
import sequtils, strutils, algorithm, math, future, sets, queues, tables # for AtCoder (0.13.0)
template getLine: string = stdin.readLine
template getInteger: int = getLine.parseInt
template getBiggestInteger: int64 = getLine.parseBiggestInt
template getIntSeq: seq[int] = getLine.split.map(parseInt)
template getBigIntSeq: seq[int64] = getLine.split.map(parseBiggestInt)

proc dfs(num_array: seq[int], left, right, center, rest: var seq[int]): void =
  if rest.len == 0:
    assert(left.len == right.len)
    if num_array.len mod 2 == 1:
      assert(center.len == 1)

    let generated_pairs = left.zip(right).mapIt((num_array[it[0]], num_array[it[1]]))
    generated_pairs.echo
  elif center.len == 0 and num_array.len mod 2 == 1:
    center.add(rest.pop)
    dfs(num_array, left, right, center, rest)
    for i in 0..<rest.len:
      swap(center[0], rest[i])
      dfs(num_array, left, right, center, rest)
      swap(center[0], rest[i])
    rest.add(center.pop)
  else:
    left.add(rest.pop)
    right.add(rest.pop)
    dfs(num_array, left, right, center, rest)
    for i in 0..<rest.len:
      swap(right[^1], rest[i])
      dfs(num_array, left, right, center, rest)
      swap(right[^1], rest[i])
    rest.add(right.pop)
    rest.add(left.pop)

proc pair_enumeration(num_array: seq[int]): void =
  var
    left, right, center = newSeq[int]()
    rest = toSeq(0..<num_array.len)
  dfs(num_array, left, right, center, rest)

when isMainModule:
  pair_enumeration(@[1, 2, 3, 4])
  echo()
  pair_enumeration(@[1, 2, 3, 4, 5])

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

