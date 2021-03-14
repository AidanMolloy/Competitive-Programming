#include <bits/stdc++.h>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;

	int num1, num2;
	num1 = 2;
	num2 = 1;
	for(int i = 0;i<n;i++){
		num1 += num2;
		num2 *= 2;
	}

	cout << num1 * num1;

	return 0;
}
