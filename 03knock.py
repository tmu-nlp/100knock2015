#!/usr/bin/python
# _*_ coding: utf-8 _*_

#円周率

#a ="a, b, c, d, e"
#a.replace(",", "")
#print a

original = "Now I need a drink, alcoholic of course, after the heavy lectures involiving quantum mechanics."
#print original

#original_kai = original.strip(",").strip(".")
#print original_kai
#originalは文字列なのに, stripメソッドによって "," と"."が削除されない
#### stripメソッドは両端のみ！！！！

#original.replace(",", "")      original.replaceには戻り値がある
#print original               　ので変数に入れなければならない
#original.replace(".", "")　　　文字列のメソッドはだいたいそうなのかな？？
#print original        

original = original.replace(".","")
original = original.replace(",","")

my_list = original.split(" ")
#print my_list

p_list = [len(my_list[index]) for index in range(len(my_list))]

print p_list


