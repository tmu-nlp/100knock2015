import sys

for line in open(sys.argv[1], "r"):
    print line.expandtabs(1)

