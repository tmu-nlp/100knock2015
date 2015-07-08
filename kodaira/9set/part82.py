#!usr/bin/python


from random import randint
import bz2

fout = open('pair.txt', 'w')

def make_start_end(random_int, num, length):
    start = num - random_int if num > random_int else 0
    end = num + 1 + random_int
    if num > length - 1:
        num = length - 1
    if end > length - 1:
        return start, length - 1, sstart
    return start, end, num

print 'Load file....'
corpus = bz2.decompress(open('corpus2.bz2', 'rb').read() ).split()

print 'finish load file!'
context_length = len(corpus)

print 'write file at first'
for num in range(5, context_length - 5):
    rand_int = randint(2, 5)
    fout.write(corpus[num] + '\t' + '\t'.join([corpus[i] \
        for i in range(num - rand_int, num) + \
        range(num + 1, num + 1 + rand_int)]) + '\n')

print 'write file at second'
for num in range(5) + range(context_length - 5, context_length + 1):
    start, end, sstart = make_start_end(randint(2, 5), num + 1, context_length)
    try:
        fout.write(corpus[num] + '\t' + '\t'.join([corpus[i] \
            for i in range(start, num) + range(sstart, end)]) + '\n')
    except:
        continue
fout.close()


            

 
