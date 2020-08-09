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


# :warning: nim-library/scc.nim

<a href="../../index.html">Back to top page</a>

* category: <a href="../../index.html#dd390cd6b7c8b7d7cfc5543fc36ddaac">nim-library</a>
* <a href="{{ site.github.repository_url }}/blob/master/nim-library/scc.nim">View this file on GitHub</a>
    - Last commit date: 2020-08-09 18:21:38+09:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
import algorithm, complex, future, macros, math, queues, rationals, sets, sequtils, strutils, tables # for 0.13.0
# import algorithm, bitops, complex, deques, heapqueue, lenientops, macros, math, queues, rationals, sets, sequtils, strformat, strscans, strutils, sugar, tables # for 0.19

# ----- input macro by nimon -----

macro unpack*(input: seq; count: static[int]): untyped =
  result = quote do: ()
  when NimMinor <= 13:
    for i in 0..<count: result[0].add quote do: `input`[`i`]
  else:
    for i in 0..<count: result.add quote do: `input`[`i`]

## count == 0 のとき unpackしない(seq)
## count >  0 のとき count個分 unpack した結果の tuple を返す
type UnselectableTypeError = object of Exception
template input*(typ: typedesc; count: Natural = 0): untyped =
  let line = stdin.readLine.split
  when count == 0:
    when typ is int:    line.map(parseInt)
    elif typ is float:  line.map(parseFloat)
    elif typ is string: line
    else: raise newException(UnselectableTypeError, "You selected a type other than int, float or string")
  else:
    when typ is int:    line.map(parseInt).unpack(count)
    elif typ is float:  line.map(parseFloat).unpack(count)
    elif typ is string: line.unpack(count)
    else: raise newException(UnselectableTypeError, "You selected a type other than int, float or string")

# 2-dim table
template inputs*(typ: typedesc; count = 0; rows = 1): untyped =
  (1..rows).mapIt(input(typ, count))

# ----- end input macro -----

# from https://nim-lang.org/docs/manual.html#macros-expression-macros
# when NimMinor >= 16, you can use future.dump (sugar.dump)
macro debug(args: varargs[untyped]): untyped =
  result = nnkStmtList.newTree()
  for n in args:
    result.add newCall("write", newIdentNode("stderr"), newLit(n.repr))
    result.add newCall("write", newIdentNode("stderr"), newLit(": "))
    result.add newCall("write", newIdentNode("stderr"), n)
    result.add newCall("writeLine", newIdentNode("stderr"), newLit(""))

const MOD = 10^9 + 7
const INF = high(int)

type
  StronglyConnectedComponents = object
    graph, rev_graph: seq[seq[int]]
    vs, comp, sorted_vs: seq[int]
    used: seq[bool]

proc initSCC(size: Natural): StronglyConnectedComponents =
  return StronglyConnectedComponents(
    graph: newSeqWith(size, newSeq[int]()),
    rev_graph: newSeqWith(size, newSeq[int]()),
    vs: newSeq[int](),
    comp: newSeq[int](size),
    sorted_vs: newSeq[int](size),
    used: newSeq[bool](size)
  )

proc add_edge(scc: var StronglyConnectedComponents, v1: int, v2: int) =
  scc.graph[v1].add(v2)
  scc.rev_graph[v2].add(v1)

proc dfs(scc: var StronglyConnectedComponents, v: int) =
  scc.used[v] = true
  for c in scc.graph[v]:
    if not scc.used[c]:
      scc.dfs(c)
  scc.vs.add(v)

proc rev_dfs(scc: var StronglyConnectedComponents, v: int, k: int) =
  scc.used[v] = true
  scc.comp[v] = k
  for c in scc.rev_graph[v]:
    if (not scc.used[c]):
      scc.rev_dfs(c, k)

proc run(scc: var StronglyConnectedComponents): int =
  scc.used.fill(false)
  for v in 0..<scc.graph.len:
    if not scc.used[v]:
      scc.dfs(v)
  scc.used.fill(false)
  var k = 0
  for v in scc.vs.reversed:
    if not scc.used[v]:
      scc.rev_dfs(v, k)
      k.inc
  for i, v in scc.comp:
    scc.sorted_vs[v] = i
  return k

when isMainModule:
  let
    (N, M) = input(int, 2)
  var scc = initSCC(N)
  for i in 0..<(N - 1 + M):
    let (a, b) = input(int, 2)
    scc.add_edge(a, b)
  scc.run()
  debug(scc.sorted_vs)

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

