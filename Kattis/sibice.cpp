#include <bits/stdc++.h>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	double n, w, h;
	cin >> n >> w >> h;

	double hypot = sqrt(w*w + h*h);

	for(int i = 0; i < n; i++){
		double x;
		cin >> x;
		if(x <= hypot){
			cout << "DA" << "\n";
		}else{
			cout << "NE" << "\n";
		}

	}

	return 0;
}
