if __name__ == '__main__':
    sent = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    head = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    elem = dict()
    for i, tok in enumerate(sent.split()):
        if i + 1 in head:
            elem[tok[0]] = i+1
        else:
            elem[tok[0:2]] = i+1
    for k, v in sorted(elem.items(), key=lambda x:x[1]):
        print k, v
