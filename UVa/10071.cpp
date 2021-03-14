#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

//memset(memo, -1, sizeof memo);
//vi memo(n, -1);
//memset(arr, 0, sizeof arr);

const int INF = 1e9;
const ll LLINF = 4e18;
const double EPS = 1e-9;

// ++i;
// ans = a ? b : c;
// ans += val;
// index = (index + 1) % n;
// index = (index + n - 1) % n;
// int ans = (int)((double)d + 0.5);
// ans = min(ans, new_computation);

int main() {
  int a, b;
  while(scanf("%d %d", &a, &b) != EOF){
    printf("%d\n", 2 * a * b);
  }
  return 0;
}
