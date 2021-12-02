#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

vector<int> depths;

int part1(){
    int count = 0;
    for(int i = 0; i < depths.size()-1; i++){
        if(depths[i+1] > depths[i]) {
            count++;
        }
    }
    return count;
}

int part2(){
    int count = 0;
    for(int i = 0; i < depths.size()-3; i++){
        int sumA = depths[i] + depths[i+1] + depths[i+2];
        int sumB = depths[i+1] + depths[i+2] + depths[i+3];
        if(sumB > sumA) {
            count++;
        }
    }
    return count;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("solution.txt", "w", stdout);

    int input;
    while(cin >> input){
        depths.push_back(input);
    }

    cout << "Part 1: " << part1() << "\n";
    cout << "Part 2: " << part2() << "\n";
 
    return 0;
}