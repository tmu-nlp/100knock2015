#coding:utf-8

file_1 = open("col1.txt", "r")
file_2 = open("col2.txt", "r")
new_txt = open("new_col.txt", "w")

for line1, line2 in zip(file_1, file_2):
    print line1.strip(),"\t",line2.strip()

    word = str(file_1) + "\t" + str(file_2) + "\n"
    new_txt.write(word)

