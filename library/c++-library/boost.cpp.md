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


# :warning: c++-library/boost.cpp

<a href="../../index.html">Back to top page</a>

* category: <a href="../../index.html#97d0d85922e0aae2441e69f2870930aa">c++-library</a>
* <a href="{{ site.github.repository_url }}/blob/master/c++-library/boost.cpp">View this file on GitHub</a>
    - Last commit date: 1970-01-01 00:00:00+00:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
#define IGNORE

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/numeric/ublas/io.hpp>
#include <boost/numeric/ublas/matrix.hpp>

using mpi = boost::multiprecision::int128_t;
// using mpi = boost::multiprecision::cpp_int // 任意桁

using namespace boost::numeric;
using imatrix = ublas::matrix<mpi>;
// 行列積は ublas::prod
// imatrix mat(N, M);
// mat(N, M) = 2;

```
{% endraw %}

<a id="bundled"></a>
{% raw %}
```cpp
#line 1 "c++-library/boost.cpp"
#define IGNORE

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/numeric/ublas/io.hpp>
#include <boost/numeric/ublas/matrix.hpp>

using mpi = boost::multiprecision::int128_t;
// using mpi = boost::multiprecision::cpp_int // 任意桁

using namespace boost::numeric;
using imatrix = ublas::matrix<mpi>;
// 行列積は ublas::prod
// imatrix mat(N, M);
// mat(N, M) = 2;

```
{% endraw %}

<a href="../../index.html">Back to top page</a>

