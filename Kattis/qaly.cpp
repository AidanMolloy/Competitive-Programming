#include <bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n;
	cin >> n;
	double qaly = 0;
	for(int i=0;i<n;i++){
		double x, y;
		cin >> x >> y;
		qaly += (x*y);
	}

	cout << qaly;

	return 0;
}
