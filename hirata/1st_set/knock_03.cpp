//knock_03.cpp
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

vector<int> word_count(string str){
    vector<int> v;
    istringstream sstr(str);
    string buffer;
    while(getline(sstr, buffer, ' ')){
        if(buffer.substr(buffer.size()-1,1) == "." or buffer.substr(buffer.size()-1,1) == ","){
            buffer = buffer.substr(0,buffer.size()-1);
        }
        v.push_back(buffer.size());
    }
    return v;
}

int main(){
    string pi_str("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.");
    vector<int> answer_v = word_count(pi_str);
    for(int i = 0; i < answer_v.size(); i++)
        cout << answer_v[i] << endl;
}
