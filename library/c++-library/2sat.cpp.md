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


# :warning: c++-library/2sat.cpp

<a href="../../index.html">Back to top page</a>

* category: <a href="../../index.html#97d0d85922e0aae2441e69f2870930aa">c++-library</a>
* <a href="{{ site.github.repository_url }}/blob/master/c++-library/2sat.cpp">View this file on GitHub</a>
    - Last commit date: 2020-08-09 18:21:38+09:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

struct StronglyConnectedComponents {
  int V;
  std::vector<std::vector<int>> G, rG;
  std::vector<int> vs, cmp;
  std::vector<bool> used;

  StronglyConnectedComponents(const int V)
      : V(V), G(V), rG(V), cmp(V), used(V) {}

  void add_edge(const int from, const int to) {
    G[from].push_back(to);
    rG[to].push_back(from);
  }

  void dfs(const int v) {
    used[v] = true;
    for (int c : G[v])
      if (not used[c]) dfs(c);
    vs.push_back(v);
  }

  void rdfs(const int v, const int k) {
    used[v] = true;
    cmp[v] = k;
    for (int c : rG[v])
      if (not used[c]) rdfs(c, k);
  }

  int run() {
    std::fill(used.begin(), used.end(), false);
    vs.clear();
    for (int v = 0; v < V; v++)
      if (!used[v]) dfs(v);
    std::fill(used.begin(), used.end(), false);
    int k = 0;
    for (int i = vs.size() - 1; i >= 0; i--)
      if (!used[vs[i]]) rdfs(vs[i], k++);
    return k;
  }

  std::vector<int> create_order() {
    std::vector<int> order(V);
    for (std::size_t i = 0; i < cmp.size(); i++) {
      order[cmp[i]] = i;
    }
    return order;
  }
};

struct TwoSat : StronglyConnectedComponents {
  int N;
  std::vector<bool> ans;
  TwoSat(const int N) : StronglyConnectedComponents(2 * N + 1), N(N), ans(N) {}

  void add_constraint(int a, int b) {
    add_edge(neg(a), pos(b));
    add_edge(neg(b), pos(a));
  }
  int pos(const int v) { return v > 0 ? v : N - v; }
  int neg(const int v) { return v > 0 ? N + v : -v; }

  bool run() {
    StronglyConnectedComponents::run();
    for (int i = 1; i <= N; i++) {
      if (cmp[i] == cmp[i + N]) {
        return false;
      }
    }

    for (int i = 1; i <= N; i++) {
      ans[i - 1] = cmp[i] > cmp[i + N];
    }
    return true;
  }
};

void yosupo() {
  // https://judge.yosupo.jp/problem/scc
  std::string s;
  std::cin >> s >> s;
  int N, M;
  std::cin >> N >> M;
  TwoSat sat(N);
  for (int i = 0; i < M; i++) {
    int a, b, c;
    std::cin >> a >> b >> c;
    sat.add_constraint(a, b);
  }
  if (!sat.run()) {
    std::cout << "s UNSATISFIABLE" << std::endl;
  } else {
    std::cout << "s SATISFIABLE\nv ";
    for (int i = 0; i < N; i++) {
      std::cout << (sat.ans[i] ? i + 1 : -(i + 1)) << ' ';
    }
    std::cout << '0' << std::endl;
  }
}

int main() {
  std::cin.tie(0);
  std::ios_base::sync_with_stdio(false);

  yosupo();
  return 0;
}
```
{% endraw %}

<a id="bundled"></a>
{% raw %}
```cpp
#line 1 "c++-library/2sat.cpp"
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

struct StronglyConnectedComponents {
  int V;
  std::vector<std::vector<int>> G, rG;
  std::vector<int> vs, cmp;
  std::vector<bool> used;

  StronglyConnectedComponents(const int V)
      : V(V), G(V), rG(V), cmp(V), used(V) {}

  void add_edge(const int from, const int to) {
    G[from].push_back(to);
    rG[to].push_back(from);
  }

  void dfs(const int v) {
    used[v] = true;
    for (int c : G[v])
      if (not used[c]) dfs(c);
    vs.push_back(v);
  }

  void rdfs(const int v, const int k) {
    used[v] = true;
    cmp[v] = k;
    for (int c : rG[v])
      if (not used[c]) rdfs(c, k);
  }

  int run() {
    std::fill(used.begin(), used.end(), false);
    vs.clear();
    for (int v = 0; v < V; v++)
      if (!used[v]) dfs(v);
    std::fill(used.begin(), used.end(), false);
    int k = 0;
    for (int i = vs.size() - 1; i >= 0; i--)
      if (!used[vs[i]]) rdfs(vs[i], k++);
    return k;
  }

  std::vector<int> create_order() {
    std::vector<int> order(V);
    for (std::size_t i = 0; i < cmp.size(); i++) {
      order[cmp[i]] = i;
    }
    return order;
  }
};

struct TwoSat : StronglyConnectedComponents {
  int N;
  std::vector<bool> ans;
  TwoSat(const int N) : StronglyConnectedComponents(2 * N + 1), N(N), ans(N) {}

  void add_constraint(int a, int b) {
    add_edge(neg(a), pos(b));
    add_edge(neg(b), pos(a));
  }
  int pos(const int v) { return v > 0 ? v : N - v; }
  int neg(const int v) { return v > 0 ? N + v : -v; }

  bool run() {
    StronglyConnectedComponents::run();
    for (int i = 1; i <= N; i++) {
      if (cmp[i] == cmp[i + N]) {
        return false;
      }
    }

    for (int i = 1; i <= N; i++) {
      ans[i - 1] = cmp[i] > cmp[i + N];
    }
    return true;
  }
};

void yosupo() {
  // https://judge.yosupo.jp/problem/scc
  std::string s;
  std::cin >> s >> s;
  int N, M;
  std::cin >> N >> M;
  TwoSat sat(N);
  for (int i = 0; i < M; i++) {
    int a, b, c;
    std::cin >> a >> b >> c;
    sat.add_constraint(a, b);
  }
  if (!sat.run()) {
    std::cout << "s UNSATISFIABLE" << std::endl;
  } else {
    std::cout << "s SATISFIABLE\nv ";
    for (int i = 0; i < N; i++) {
      std::cout << (sat.ans[i] ? i + 1 : -(i + 1)) << ' ';
    }
    std::cout << '0' << std::endl;
  }
}

int main() {
  std::cin.tie(0);
  std::ios_base::sync_with_stdio(false);

  yosupo();
  return 0;
}

```
{% endraw %}

<a href="../../index.html">Back to top page</a>

