//knock_06.cpp
//"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を,それぞれ, XとYとして求め,XとYの和集合,積集合,差集合を求めよ.さらに,'se'というbi-gramがXおよびYに含まれるかどうかを調べよ.
//Todo:テンプレート使ってみる．同じ操作してるので，クラス化してみるとか．
#include <iostream>
#include <string>
#include <list>
#include <set>
using namespace std;

list<string> letter_n_gram(string str, int n){
    list<string> answer_lst;
    for(int i = 0; i < str.size() - n + 1; i++){
        //cout << str.substr(i, n) << endl;
        answer_lst.push_back(str.substr(i, n));
    }
    return answer_lst;
}

// 和集合
void create_union(list<string> lst1, list<string> lst2){
    set<string> union_set;
    for(auto itr = lst1.begin(); itr != lst1.end(); ++itr){
        union_set.insert(*itr);
    }
    for(auto itr = lst2.begin(); itr != lst2.end(); ++itr){
        union_set.insert(*itr);
    }
    for(auto itr = union_set.begin(); itr != union_set.end(); ++itr){
        cout << *itr << endl;
    }
}

//積集合
void create_product(list<string> lst1, list<string> lst2){
    set<string> middle_set;
    set<string> product_set;
    for(auto itr = lst1.begin(); itr != lst1.end(); ++itr){
        middle_set.insert(*itr);
    }
    for(auto itr = lst2.begin(); itr != lst2.end(); ++itr){
        set<string>::iterator iti = middle_set.find(*itr);
        if(iti != middle_set.end()){
            product_set.insert(*itr);
        }
    }
    for(auto itr = product_set.begin(); itr != product_set.end(); ++itr){
        cout << *itr << endl;
    }
}

//差集合
void create_diff(list<string> lst1, list<string> lst2){
    set<string> middle_set;
    set<string> diff_set;
    for(auto itr = lst1.begin(); itr != lst1.end(); ++itr){
        middle_set.insert(*itr);
    }
    for(auto itr = lst2.begin(); itr != lst2.end(); ++itr){
        set<string>::iterator iti = middle_set.find(*itr);
        if(iti == middle_set.end()){
            diff_set.insert(*itr);
        }
    }
    for(auto itr = diff_set.begin(); itr != diff_set.end(); ++itr){
        cout << *itr << endl;
    }
}

int main(){
    string str_x("paraparaparadise");
    string str_y("paragraph");
    list<string> bigram_x = letter_n_gram(str_x, 2);
    list<string> bigram_y = letter_n_gram(str_y, 2);
    create_diff(bigram_x, bigram_y);
}
