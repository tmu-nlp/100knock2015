
import knock_005

my_sent1 = "paraparaparadise"
my_sent2 = "paragraph"

char_bi_list1 = knock_005.char_bi(my_sent1)
char_bi_list2 = knock_005.char_bi(my_sent2)
char_bi_set1 = set(char_bi_list1)
char_bi_set2 = set(char_bi_list2)

print "sum  %s" % (set(char_bi_list1 + char_bi_list2))
print "product  %s" % (char_bi_set1 & char_bi_set2)
print "(1)-(2)  %s" % (char_bi_set1 - char_bi_set2)
print "(2)-(1)  %s" % (char_bi_set2 - char_bi_set1)

if "se" in char_bi_set1:
    print 'char_bi_set1 have "se"'
if "se" in char_bi_set2:
    print 'char_bi_set2 have "se"'
