#!usr/bin/python

from collections import defaultdict

def spiaman(dicta, dictb):
    d = int()
    n = len(dicta)
    for num in range(n):
        d += (dicta[num] - dictb[num]) ** 2
    return 1 - float(6 * d) / (n ** 3 + n)
        
def get_rank(tuple_list):
    rank_dict = defaultdict(lambda: len(rank_dict) )
    for num, sim in sorted(tuple_list, key = lambda x: -x[1]):
        rank_dict[num]
    return rank_dict

def make_list(file_name):
    h_sim_id = list(); s_sim_id = list()
    flag = True
    for num, line in enumerate(open(file_name) ):
        if flag:
            flag = False
            continue
        w1, w2, s1, s2 = line.strip().split('\t')
        h_sim_id.append((num, float(s1) ) )
        s_sim_id.append((num, float(s2) ) )
    return get_rank(h_sim_id), get_rank(s_sim_id)

if __name__ == '__main__':
    file_name = '94_ana.txt'
    a, b = (make_list(file_name) )
    print spiaman(a, b)
