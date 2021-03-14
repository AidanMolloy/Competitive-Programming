#include <bits/stdc++.h>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	double x1, x2, y1, y2, p;
	cin >> x1;
	while(x1 != 0){
		cin >> y1 >> x2 >> y2 >> p;
		double ans1 = pow(abs(x1-x2),p);
		double ans2 = pow(abs(y1-y2),p);
		ans1 += ans2;
		double getPow = 1/p;
		ans1 = pow(ans1,getPow);
		cout << ans1 << "\n";
		cin >> x1;
	}
	return 0;
}
