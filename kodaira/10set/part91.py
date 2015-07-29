fout = open('family.txt', 'w')
flag = False
for line in open('analogy.txt'):
   if ': family' in line:
       flag = True
   elif flag:
       if ':' in line:
           flag = False
   if flag:
       fout.write(line)
