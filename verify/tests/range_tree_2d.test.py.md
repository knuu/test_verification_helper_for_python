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


# :x: tests/range_tree_2d.test.py

<a href="../../index.html">Back to top page</a>

* category: <a href="../../index.html#b61a6d542f9036550ba9c401c80f00ef">tests</a>
* <a href="{{ site.github.repository_url }}/blob/master/tests/range_tree_2d.test.py">View this file on GitHub</a>
    - Last commit date: 1970-01-01 00:00:00+00:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
# verify-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_C
# verify-helper: IGNORE
import sys
input = sys.stdin.buffer.readline

from python_library.data_structures.range_tree_2d import RangeTree2D


def main() -> None:
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    rt = RangeTree2D()
    rt.build(points)
    for _ in range(int(input())):
        x1, x2, y1, y2 = map(int, input().split())
        output = []
        rt.query((x1, x2), (y1, y2), output)
        if output:
            output.sort()
            print(*output, sep="\n")
        print()


if __name__ == "__main__":
    main()

```
{% endraw %}

<a id="bundled"></a>
{% raw %}
```cpp
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.8.5/x64/lib/python3.8/site-packages/onlinejudge_verify/docs.py", line 349, in write_contents
    bundled_code = language.bundle(self.file_class.file_path, basedir=pathlib.Path.cwd())
  File "/opt/hostedtoolcache/Python/3.8.5/x64/lib/python3.8/site-packages/onlinejudge_verify/languages/python.py", line 67, in bundle
    raise NotImplementedError
NotImplementedError

```
{% endraw %}

<a href="../../index.html">Back to top page</a>

