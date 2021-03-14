#include <bits/stdc++.h>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int x, n, mb;
	cin >> x >> n;
	mb = x;
	for(int i = 0; i < n; i++){
		int a;
		cin >> a;
		mb = mb + x - a;
	}
	cout << mb;
	return 0;
}
