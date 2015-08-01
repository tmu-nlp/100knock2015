#usr/bin/python
#coding:utf-8
import pickle
from sklearn.decomposition import TruncatedSVD


def main():
    matrix,t_set = pickle.load(open('part84.dump'))
    decomp = TruncatedSVD(n_components=300)
    decomp.fit(matrix)
    matrix = decomp.transform(matrix)
    pickle.dump([matrix,t_set],open('part85.dump','w'))

if __name__ == '__main__':
    main()
