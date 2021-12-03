#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> reports;

int toDecimal(long n)
{
    long num = n;
    int dec_value = 0;
 
    int base = 1;
 
    long temp = num;
    while (temp) {
        int last_digit = temp % 10;
        temp = temp / 10;
 
        dec_value += last_digit * base;
 
        base = base * 2;
    }
 
    return dec_value;
}

vector<string> removeOccurences(vector<string> temp, int cursor, char x){
    int i = 0;
    while(i < temp.size()){
        if(temp[i][cursor] == x){
            temp.erase(temp.begin()+i);
        }else{
            i++;
        }
    }
    return temp;
}

long mostCommonValue(vector<string> temp){
    int cursor = 0;
    while(temp.size() > 1){
        int count = 0;
        for(int i = 0; i < temp.size();i++){
            int val = temp[i][cursor] - '0';
            count += val;
        }
        if(count >= (temp.size()+1)/2){
            temp = removeOccurences(temp, cursor, '0');
        }else{
            temp = removeOccurences(temp, cursor, '1');
        }
        cursor++;
    }
    return stol(temp[0]);
}

long leastCommonValue(vector<string> temp){
    int cursor = 0;
    while(temp.size() > 1){
        int count = 0;
        for(int i = 0; i < temp.size();i++){
            int val = temp[i][cursor] - '0';
            count += val;
        }
        if(count >= (temp.size()+1)/2){
            temp = removeOccurences(temp, cursor, '1');
        }else{
            temp = removeOccurences(temp, cursor, '0');
        }
        cursor++;
    }
    return stol(temp[0]);
}

int part1(){
    int commonality[12] = {0};
    for(int i = 0; i<reports.size();i++){
        for(int j = 0; j<reports[i].size();j++){
            int val = reports[i][j] - '0';
            commonality[j] += val;
        }
    }
    long gamma = 0, epsilon = 0;
    for(int i=0;i<12;i++){
        gamma *= 10;
        epsilon *= 10;
        if(commonality[i] > reports.size()/2){
            gamma += 1;
        }else{
            epsilon += 1;
        }
    }
    return toDecimal(gamma) * toDecimal(epsilon);
}

int part2(){
    return toDecimal(mostCommonValue(reports)) * toDecimal(leastCommonValue(reports));
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("solution.txt", "w", stdout);

    string input;
    while(cin >> input){
        reports.push_back(input);
    }

    cout << "Part 1: " << part1() << "\n";
    cout << "Part 2: " << part2() << "\n";
 
    return 0;
}