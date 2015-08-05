#!usr/bin/python

import random
from collections import defaultdict


def random_cluster(country_name_list):
    cluster_list = list() 
    for num, country in enumerate(country_name_list):
        cluster_list.append((num, country, random.randint(0, 4) ) )
    return cluster_list


def get_center_vector(cluster_list, country_vec_list):
    center_vec = 0
    cluster_count = defaultdict(int)
    vec_list = [numpy.zeros(len(country_vec_list[0]) ) for i in range(5)]
    for list_id, country, cluster in cluster_list:
        cluster_count[cluster] += 1
        vec_list[cluster] += country_vec_list[list_id]
    for cluster, num in cluster_count.items():
        vec_list[cluster] /= num
    print vec_list
    return vec_list
        

def get_min(center_vec_list, country_vec):
    min_vec = (9999999999999, 4)
    for num, vec in enumerate(center_vec_list):
        if numpy.linalg.norm(vec + country_vec) < min_vec[0]:
            min_vec = (numpy.linalg.norm(vec + country_vec), num)
    return min_vec[1]


def update_cluster_list(cluster_list, country_vec_list, center_vec_list):
    new_cluster_list = list(cluster_list)
    flag = False
    for list_id, country, cluster in cluster_list:
        new_cluster = get_min(center_vec_list, country_vec_list[list_id])
        if new_cluster != cluster: 
           new_cluster_list[list_id] = \
               (new_cluster_list[list_id][0], new_cluster_list[list_id][1], \
               new_cluster)
           flag = True
    return new_cluster_list, flag

def k_means(country_name_list, country_vec_list):
    cluster_list = random_cluster(country_name_list)
    count = 0
    while 1:
        count += 1
        center_vec_list = get_center_vector(cluster_list, country_vec_list)
        new_cluster_list, flag = \
            update_cluster_list(cluster_list, country_vec_list, center_vec_list)
        if flag:
            if count == 3:
                print 'iteration_1000'
                break
            cluster_list = new_cluster_list
        else:
            print 'finish' + str(count)
            break
    return cluster_list

from part96 import *
import pickle
if __name__ == '__main__':
    #matrix_data = load_vec('vector.csv')
    #voc = open('word.txt').read().split('\n')
    country_data = pickle.load(open('country_data.pkl') )
    voc, matrix_data = country_data
    cluster_list = k_means(voc, matrix_data)
    cluster = defaultdict(lambda: list())
    for list_id, country, cluster_id in cluster_list:
        cluster[cluster_id].append(country)
    for cluster_id, country in cluster.items():
        print cluster_id, country
