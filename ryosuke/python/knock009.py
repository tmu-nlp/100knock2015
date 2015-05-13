import random

if __name__ == '__main__':
    sent = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    shuf_sent = list()
    for tok in sent.split():
        if len(tok) <= 4:
            shuf_sent.append(tok)
        else:
            head = tok[0]
            middle = list(tok[1:-1])
            tail = tok[-1]
            random.shuffle(middle)
            tok = '%s%s%s' % (head, ''.join(middle), tail)
            shuf_sent.append(tok)
    print ' '.join(shuf_sent)

