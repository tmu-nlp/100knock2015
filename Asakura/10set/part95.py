#!/usr/bin/python
#coding:utf-8



def main():
    input_file = open('part94.txt')
    human_score_dict = dict()
    word2vec_score_dict = dict()
    human_rank_dict = dict()
    word2vec_rank_dict = dict()
    word_list = list()
    for line in input_file:
        word_score,word2vec_score = line.strip().split()
        word_list.append(word_score.split(',')[0]+'_'+word_score.split(',')[1])
        human_score_dict[word_score.split(',')[0]+'_'+word_score.split(',')[1]] = float(word_score.split(',')[2]) 
        word2vec_score_dict[word_score.split(',')[0]+'_'+word_score.split(',')[1]] = float(word2vec_score)
    for num,(word,score) in enumerate(sorted(human_score_dict.items(), key=lambda x:-x[1]),start=1):
        human_rank_dict[word] = num
    for num,(word,score) in enumerate(sorted(word2vec_score_dict.items(), key=lambda x:-x[1]),start=1):
        word2vec_rank_dict[word] = num
    D2 = 0
    N = len(word2vec_rank_dict.keys())
    for word in word_list:
        D2 += (abs(human_rank_dict[word]-word2vec_rank_dict[word]))**2
    P = 1-6*D2/float(N**3-N)
    print 'スピアマンの相関係数:%f'%P

if __name__ == '__main__':
    main()
