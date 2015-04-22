# coding:utf-8
if __name__=='__main__':
    tok1 = u'パトカー'
    tok2 = u'タクシー'
    tok3 = u''
    for c1, c2 in zip(tok1, tok2):
        tok3 += c1 + c2
    print tok3
