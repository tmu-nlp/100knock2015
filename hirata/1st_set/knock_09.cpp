//knock_09.cpp
//スペースで区切られた単語列に対して,各単語の先頭と末尾の文字は残し,それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ.ただし,長さが4以下の単語は並び替えないこととする.適当な英語の文(例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")を与え,その実行結果を確認せよ.
//
//配列のシャッフルは http://file.ujilog.blog.shinobi.jp/main.html#tagC6 を参照
#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <sstream>
#include <unordered_map>
#include <sstream>
#include<stdlib.h>
using namespace std;

#define LENG 10

void shafle(string str){
    vector<string> words_vec;
    istringstream sstr(str);
    string buffer;
    while(getline(sstr, buffer, ' ')){
        words_vec.push_back(buffer);
        cout << buffer << endl; 
        for (int i = 0; i < sizeof(buffer); i++) {
            int r = rand() % (sizeof(buffer) - i) + i;
            char tmp = buffer[i];
            buffer[i] = buffer[r];
            buffer[r] = tmp;
        }
        cout << buffer << endl; 
    }
}

int main(){
    string input_str("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind.");
    shafle(input_str);
}
