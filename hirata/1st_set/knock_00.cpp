//knock_00.cpp
#include <string>
#include <iostream>
using namespace std;

void str_reverse(string input_str){
    for (int i = input_str.size() -1 ; i >= 0; i--)
        cout << input_str[i];
    cout << endl;
}

int main(){
    string test_str("stressed");
    str_reverse(test_str);
}
