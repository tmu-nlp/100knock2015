//knock_08.cpp
//与えられた文字列の各文字を,以下の仕様で変換する関数cipherを実装せよ.
//
//英小文字ならば(219 - 文字コード)の文字に置換
//その他の文字はそのまま出力
//この関数を用い,英語のメッセージを暗号化・復号化せよ.
#include <iostream>
#include <sstream>
#include <string>
#include <ctype.h>
using namespace std;

int main() {
    //ostringstream stream;
    //stream << static_cast<char>(0x42) << static_cast<char>(0x41);
    //string ss = stream.str();
    //cout << '[' << ss << ']' << endl;
    //char c = 'A';
    //int a = c;
    //string s("Abc");
    //cout << (int)c << endl;
    char str[] = "Aa Bb 1-2*3 Cc";
    for(int i = 0; i < sizeof(str); i++){
        if(islower(str[i]) != 0){
            cout << (int)str[i];
        }
        else cout << str[i];
    }
    cout << endl;
}
