#include <bits/stdc++.h>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	string x;
	cin >> x;

	for(int i=1;i<x.size();i++){
		if (x[i-1] == 's' &&  x[i] == 's'){
			cout << "hiss";
			return 0;
		}
	}
	cout << "no hiss";
	return 0;
}
