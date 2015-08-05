#!usr/bin/python

def culc_prec(text_name):
    check = lambda w_list: w_list[3] == w_list[4]
    ans = [1 if line.split()[3] == line.split()[4] else 0 \
        for line in open(text_name)]
    print ans.count(1) / float(len(ans) )

if __name__ == '__main__':
    #text_name = sys.argv[1]
    text_name = '92_w2v.txt' 
    culc_prec(text_name)
