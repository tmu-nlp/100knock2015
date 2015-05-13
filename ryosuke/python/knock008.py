def cipher(string):
    result = ''
    for char in string:
        if char.islower():
            result += chr(219 - ord(char))
        else:
            result += char
    return result

if __name__ == '__main__':
    s = 'Test Stringa'
    print s
    print '\nEncode'
    print cipher(s)
    print '\nDecode'
    print cipher(cipher(s))
