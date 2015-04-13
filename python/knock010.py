import sys

if __name__ == '__main__':
    count = 0
    for line in open(sys.argv[1]):
        count += 1
    print count
