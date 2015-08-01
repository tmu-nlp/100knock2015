#!usr/bin/python
#coding:utf-8


def delete_head_symbol(word):
    if not word or word[0] not in rm_list:
        return word
    else:
        word = word[1:]
        return delete_head_symbol(word)


def delete_tail_sympol(word):
    if not word or word[-1] not in rm_list:
        return word
    else:
        word = word[:-1]
        return delete_tail_sympol(word)

def main():
    train_file = open('enwiki-20150112-400-r100-10576.txt')
    output_file = open('part80.txt','w')
    for line in train_file:
        sent_list = list()
        word_list = line.strip().split()
        if not word_list:
            continue
        for word in word_list:
            word = delete_head_symbol(word)
            if not word:
                continue
            word = delete_tail_sympol(word)
            if not word:
                continue
            sent_list.append(word)
        sent = ' '.join(sent_list)
        output_file.write(sent+'\n')
    train_file.close()
    output_file.close()
if __name__ == '__main__':
    rm_list = ['.',',','!','?',';',':','(',')','[',']',"'",'"']
    main()
