#!/usr/bin/python

def n_gram(n, line):
    X = [0]*1000
    Y = [0]*1000

    for i in range(0, len(line) - n + 1):
         X[i] = str(line[i])
         for j in range(1, n):
             X[i] = str(X[i]) + str(line[i + j])

    words = line.split(" ")

    for k in range(0, len(words) - n + 1):
         Y[k] = str(words[k])
         for l in range(1, n):
             Y[k] = Y[k] + " " + str(words[k + l])

    for x in range(0, len(line) - n + 1):
         print X[x]

    for y in range(0, len(words) - n + 1):
         print Y[y]

if __name__ == "__main__":
     m = 2
     sentence = "I am an NLPer"
     n_gram(m, sentence)

