import pickle

import numpy
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


if __name__ == '__main__':
   count_names, count_vec = pickle.load(open('country_data.pkl'))
   tsne = TSNE().fit_transform(numpy.array(count_vec) )
   for (xx, yy), name, in zip(tsne, count_names):
       plt.text(xx, yy, name)
   plt.savefig('part99.png')
