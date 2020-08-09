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


# :heavy_check_mark: python_library/data_structures/matrix.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#4f7277da04114aac533381a4614f94a3">python_library/data_structures</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library/data_structures/matrix.py">View this file on GitHub</a>
    - Last commit date: 2020-08-09 10:20:24+00:00




## Verified with

* :heavy_check_mark: <a href="../../../verify/tests/matrix_determinant.test.py.html">tests/matrix_determinant.test.py</a>
* :heavy_check_mark: <a href="../../../verify/tests/matrix_mult.test.py.html">tests/matrix_mult.test.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
from copy import deepcopy


class Matrix:
    ZERO = 0
    ONE = 1

    def __init__(self, mat, copy: bool = True):
        assert len(mat) and len(mat[0])
        if copy:
            self.mat = deepcopy(mat)
        else:
            self.mat = mat

    def __matmul__(self, other):
        ret = [[self.ZERO] * len(other.mat[0]) for _ in range(len(self.mat))]
        for i in range(len(self.mat)):
            for k in range(len(self.mat[0])):
                for j in range(len(other.mat[0])):
                    ret[i][j] += self.mat[i][k] * other.mat[k][j]
        return Matrix(ret)

    def __pow__(self, k):
        ret = Matrix([[self.ZERO] * len(self.mat[0]) for _ in range(len(self.mat))])
        for i in range(len(self.mat)):
            ret.mat[i][i] = self.ONE
        n = Matrix(deepcopy(self.mat))

        while k:
            if k & 1:
                ret = ret.__matmul__(n)
            n = n.__matmul__(n)
            k >>= 1
        return ret

    @property
    def shape(self):
        return len(self.mat), len(self.mat[0])

    def __str__(self):
        return "[{}]\n".format("\n".join(str(row) for row in self.mat))


def det(mat: Matrix, mod: int = 998244353) -> int:
    # mat は変更されることに注意。
    ret = 1
    N = mat.shape[0]
    for i in range(N):
        pivot = i
        for j in range(i + 1, N):
            if abs(mat.mat[j][i]) > abs(mat.mat[pivot][i]):
                pivot = j
        mat.mat[i], mat.mat[pivot] = mat.mat[pivot], mat.mat[i]
        ret *= mat.mat[i][i] * (-1 if i != pivot else 1)
        ret %= mod
        if not mat.mat[i][i]:
            break
        inv = pow(mat.mat[i][i], mod - 2, mod)
        for j in range(i + 1, N):
            for k in reversed(range(i, N)):
                mat.mat[j][k] += mod - mat.mat[i][k] * mat.mat[j][i] % mod * inv % mod
                mat.mat[j][k] %= mod
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

