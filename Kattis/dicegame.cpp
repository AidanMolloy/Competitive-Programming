#include <bits/stdc++.h>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	double a,b,c,d;
	cin >> a >> b >> c >> d;
	double avg = ((a + b) / 2) + ((c + d) / 2);

	double e, f, g, h;
	cin >> e >> f >> g >> h;
	double avg2 = ((e + f) / 2) + ((g + h) / 2);

	if(avg > avg2){
		cout << "Gunnar";
	}else if(avg2 > avg){
		cout << "Emma";
	}else{
		cout << "Tie";
	}
	return 0;
}
