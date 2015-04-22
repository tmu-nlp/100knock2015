//knock_02.cpp
#include <iostream>
#include <locale>
using namespace std;

wstring mix_combine(wstring str1, wstring str2){
    wstring answer_str;
    for(int i = 0; i <= str1.length(); i++){
        answer_str += str1[i];
        answer_str += str2[i];
    }
    return answer_str;
}

int main(){
    setlocale(LC_CTYPE, "ja_JP.UTF-8");
    wstring str1 = L"パトカー";
    wstring str2 = L"タクシー";
    wstring answer = mix_combine(str1, str2);
    wcout << answer << endl;
}
