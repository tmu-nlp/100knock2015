if __name__=='__main__':
    sent = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    pi = list()
    for tok in sent.split():
        if tok.endswith(',') or tok.endswith('.'):
            tok = tok[:-1]
        pi.append(len(tok))
    print pi
