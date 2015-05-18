# coding:utf-8
def template(x, y, z):
    return '%s時の%sは%s' % (str(x), y, str(z))

if __name__ == '__main__':
    x = 12
    y = '気温'
    z = 22.4
    print template(x, y, z)
