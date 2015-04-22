//knock_07.cpp
//引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ.さらに,x=12, y="気温", z=22.4として,実行結果を確認せよ.
#include <iostream>
#include <string>
#include <locale>
using namespace std;

wstring str_template(wstring x, wstring y, wstring z){
    wstring str_temp;
    str_temp = x + L"時の" + y + L"は" + z;
}

int main(){
    setlocale(LC_CTYPE, "ja_JP.UTF-8");
    wstring x(L"12");
    wstring y(L"気温");
    wstring z(L"22.4");
    wstring str_temp = str_template(x, y, z);
    wcout << str_temp << endl;
}
