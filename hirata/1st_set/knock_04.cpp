//knock_04.cpp
#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <sstream>
#include <unordered_map>
#include <sstream>
using namespace std;

void chemical(string str, list<int> one_wordlst){
    vector<string> words_vec;
    istringstream sstr(str);
    string buffer;
    while(getline(sstr, buffer, ' ')){
        words_vec.push_back(buffer);
    }
    for(int i = 0; i < words_vec.size(); i++){
        if(one_wordlst.front() - 1 == i){
            cout << words_vec[i].substr(0, 1);
            one_wordlst.pop_front();
        }
        else{
            cout << words_vec[i].substr(0, 2);
        }
        cout << endl;
    }
}

int main(){
    string input_str("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.");
    list<int> one_wordlst = {1, 5, 6, 7, 8, 9, 15, 16, 19};
    one_wordlst.sort();
    chemical(input_str, one_wordlst);
}
