//knock_01.cpp
#include <string>
#include <iostream>
#include <list>
#include <locale>
using namespace std;

void patato(wstring input_str, list<int> lst){
    wstring extract_str;
    for(auto itr = lst.begin(); itr != lst.end(); itr++){
        extract_str += input_str[*itr];
        //cout << *itr << endl;
    }
    wcout << extract_str << endl;
}

int main(){
    setlocale(LC_CTYPE, "ja_JP.UTF-8");
    //string test_str(u8"パタトクカシー");
    wstring test_str = L"パタトクカシーー";
    list<int> patato_lst{1, 3, 5, 7};
    patato(test_str,patato_lst);
}
