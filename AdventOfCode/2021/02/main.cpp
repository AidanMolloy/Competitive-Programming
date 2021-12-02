#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<pair<string, int> > instructions;

int part1(){
    int horizontal = 0, depth = 0;
    for(int i = 0; i<instructions.size();i++){
        if(instructions[i].first == "forward"){
            horizontal += instructions[i].second;
        }else if(instructions[i].first == "up"){
            depth -= instructions[i].second;
        }else if(instructions[i].first =="down"){
            depth += instructions[i].second;
        }
    }
    return horizontal * depth;
}

int part2(){
    int horizontal = 0, depth = 0, aim = 0;
    for(int i = 0; i<instructions.size();i++){
        if(instructions[i].first == "forward"){
            horizontal += instructions[i].second;
            depth += aim * instructions[i].second;
        }else if(instructions[i].first == "up"){
            aim -= instructions[i].second;
        }else if(instructions[i].first =="down"){
            aim += instructions[i].second;
        }
    }
    return horizontal * depth;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("solution.txt", "w", stdout);

    string instInput;
    int distInput;
    while(cin >> instInput >> distInput){
        instructions.push_back(make_pair(instInput, distInput));
    }

    cout << "Part 1: " << part1() << "\n";
    cout << "Part 2: " << part2() << "\n";
 
    return 0;
}