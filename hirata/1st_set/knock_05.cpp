//knock_05.cpp
//与えられたシーケンス(文字列やリストなど)からn-gramを作る関数を作成せよ.この関数を用い,"I am an NLPer"という文から単語bi-gram,文字bi-gramを得よ.
//Todo:nが与えられた文字数・単語数以上だった時にエラーを返すようにする．
#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <sstream>
using namespace std;

list<string> letter_n_gram(string str, int n){
    list<string> answer_lst;
    for(int i = 0; i < str.size() - n + 1; i++){
        //cout << str.substr(i, n) << endl;
        answer_lst.push_back(str.substr(i, n));
    }
    return answer_lst;
}

list<string> word_n_gram(string str, int n){
    vector<string> words_vec;
    list<string> answer_lst;
    istringstream sstr(str);
    string buffer;
    while(getline(sstr, buffer, ' ')){
        words_vec.push_back(buffer);
    }
    for(int i = 0; i < words_vec.size() - n + 1; i++){
        string words;
        for(int j = 0; j < n; j++){
            words += words_vec[i+j];
            if(j != n-1){
                words += " ";
            }
        }
        answer_lst.push_back((words));
    }
    return answer_lst;
}

int main(){
    string input_str("I am an NLPer");
    int n = 2;
    //list<string> answer_lst = letter_n_gram(input_str,n);
    list<string> answer_lst = word_n_gram(input_str,n);
    for(auto itr = answer_lst.begin(); itr != answer_lst.end(); ++itr){
        cout << *itr << endl;
    }
}
