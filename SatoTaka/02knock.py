#!/usr/bin/python
# _*_ coding: utf-8 _*_

#「パトカー」+ 「タクシー」= 「パタトクカシーー」

pato = u"パトカー"
taku = u"タクシー"

#print pato, taku

p_list = list(pato)
t_list = list(taku)

#print p_list, t_list

patotaku = []

for index in range(len(p_list)):
    patotaku.append(p_list[index] + t_list[index])  
    print repr(patotaku).decode("unicode-escape")
#    patotaku[index] = str(patotaku[index+1])
    patotaku[index] = patotaku[index].encode("utf-8") #これはできるよ
#なぜかできない

patotaku = "".join(patotaku)
print patotaku
