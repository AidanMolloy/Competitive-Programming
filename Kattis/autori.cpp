#include <bits/stdc++.h>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	string x;
	getline(cin, x);

	string initials = "";
	for(int i=0;i<x.size();i++){
		if(isupper(x[i])){
			initials += x[i];
		}
	}
	cout << initials;
	return 0;
}
