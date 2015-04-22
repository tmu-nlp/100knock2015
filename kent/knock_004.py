str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

dict = {}
num = [1, 5, 6, 7, 8, 9, 15, 16, 19]

words = str.split()
for i in range(len(words)):
    if i+1 in num:
        j = 1
    else:
        j = 2
    dict[words[i][:j]] = i+1

    print dict
for a, b in sorted(dict.items(), key = lambda x:x[1]):
    print a, b
