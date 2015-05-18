def sent2word_bigram(sent):
    if isinstance(sent, str):
        sent = sent.split()
    sent.append('</s>')
    sent.insert(0, '<s>')

    bigram = list()
    for i in range(len(sent)-1):
        bigram.append((sent[i], sent[i+1]))
    return bigram


def sent2char_bigram(sent):
    if isinstance(sent, list):
        sent = ' '.join(sent)

    bigram = list()
    for i in range(len(sent)-1):
        bigram.append((sent[i], sent[i+1]))
    bigram.insert(0, ('<s>', sent[0]))
    bigram.append((sent[-1], '</s>'))
    return bigram


if __name__ == '__main__':
    sent1 = 'I am an NLPer'
    sent2 = ['I', 'am', 'an', 'NLPer']

    print "word bi-gram"
    for bigram in sent2word_bigram(sent1):
        print bigram
    print
    for bigram in sent2word_bigram(list(sent2)):
        print bigram
    
    print
    print 'character bi-gram'
    for bigram in sent2char_bigram(sent1):
        print bigram
    print
    for bigram in sent2char_bigram(list(sent2)):
        print bigram
