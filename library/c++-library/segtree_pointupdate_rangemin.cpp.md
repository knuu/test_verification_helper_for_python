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


# :warning: c++-library/segtree_pointupdate_rangemin.cpp

<a href="../../index.html">Back to top page</a>

* category: <a href="../../index.html#97d0d85922e0aae2441e69f2870930aa">c++-library</a>
* <a href="{{ site.github.repository_url }}/blob/master/c++-library/segtree_pointupdate_rangemin.cpp">View this file on GitHub</a>
    - Last commit date: 2020-08-09 18:21:38+09:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
const int INF = 1<<29;

/*
  RangeMinimumQuery by Segment Tree
  query:
  1. update(i, val): update i-th value to val(0-indexrd)
  2. query(low, high): find minimun value in [low, high)
  time complexity: O(log n)
  space complexity: O(2n)
  used in DSL2A(AOJ)
*/
template<typename T> struct RangeMinQuery {
  int N, _N;
  vector<T> dat;
  T initial;

  RangeMinQuery(int _N, T initial = INF) : _N(_N), initial(initial) {
    assert(_N > 0);
    N = 1;
    while (N < _N)
      N <<= 1;
    dat.assign(2 * N - 1, initial);
  }

  void update(int k, T val) {
    assert(0 <= k && k < _N);
    k += N - 1;
    dat[k] = val;

    while (k > 0) {
      k = (k - 1) / 2;
      dat[k] = min(dat[2 * k + 1], dat[2 * k + 2]);
    }
  }

  // [a, b)
  T query(int a, int b) {
    assert(0 <= a && a <= b && b <= _N);
    return query(a, b, 0, 0, N);
  }

  T query(int a, int b, int k, int l, int r) {
    if (r <= a || b <= l) return initial;
    if (a <= l && r <= b) return dat[k];

    int mid = (l + r) / 2;
    return min(query(a, b, 2 * k + 1, l, mid),
               query(a, b, 2 * k + 2, mid, r));
  }
};

```
{% endraw %}

<a id="bundled"></a>
{% raw %}
```cpp
#line 1 "c++-library/segtree_pointupdate_rangemin.cpp"
const int INF = 1<<29;

/*
  RangeMinimumQuery by Segment Tree
  query:
  1. update(i, val): update i-th value to val(0-indexrd)
  2. query(low, high): find minimun value in [low, high)
  time complexity: O(log n)
  space complexity: O(2n)
  used in DSL2A(AOJ)
*/
template<typename T> struct RangeMinQuery {
  int N, _N;
  vector<T> dat;
  T initial;

  RangeMinQuery(int _N, T initial = INF) : _N(_N), initial(initial) {
    assert(_N > 0);
    N = 1;
    while (N < _N)
      N <<= 1;
    dat.assign(2 * N - 1, initial);
  }

  void update(int k, T val) {
    assert(0 <= k && k < _N);
    k += N - 1;
    dat[k] = val;

    while (k > 0) {
      k = (k - 1) / 2;
      dat[k] = min(dat[2 * k + 1], dat[2 * k + 2]);
    }
  }

  // [a, b)
  T query(int a, int b) {
    assert(0 <= a && a <= b && b <= _N);
    return query(a, b, 0, 0, N);
  }

  T query(int a, int b, int k, int l, int r) {
    if (r <= a || b <= l) return initial;
    if (a <= l && r <= b) return dat[k];

    int mid = (l + r) / 2;
    return min(query(a, b, 2 * k + 1, l, mid),
               query(a, b, 2 * k + 2, mid, r));
  }
};

```
{% endraw %}

<a href="../../index.html">Back to top page</a>

