# coding:utf-8
if __name__=='__main__':
    s1 = u'パトカー'
    s2 = u'タクシー'
    s3 = u''
    for c1, c2 in zip(s1, s2):
        s3 += c1 + c2
    print s3
