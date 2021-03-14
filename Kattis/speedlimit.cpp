#include <bits/stdc++.h>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int a;
	while(true){
		cin >> a;
		if(a == -1){
			break;
		}
		int lastY = 0, dist = 0;
		for(int i=0;i<a;i++){
			int x, y;
			cin >> x >> y;
			dist += x * (y - lastY);
			lastY = y;
		}
		cout << dist << " miles\n";
	}
	return 0;
}
