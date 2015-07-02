import pickle


sort_weight = sorted(pickle.load(open('weight.pkl') ).items(), key = lambda x: x[1])
print 'all_num', len(sort_weight)
high_weight = sort_weight[:10]
low_weight = sort_weight[-10:]

def print_tuple_list(tuple_list):
    for left, right in tuple_list:
        print left, right

print '----------high_rank----------'
print_tuple_list(high_weight)
print '----------low_rank-----------'
print_tuple_list(low_weight)
