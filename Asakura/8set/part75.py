#!usr/bin/pyhton
#coding:utf-8


def main():
    weight_dict = dict()
    for line in open('part75_all_weight'):
        value, key = line.strip().split()
        weight_dict[key] = float(value)
    count = 0
    print '--------best_10--------'
    for key, value in sorted(weight_dict.items(), key = lambda x: -x[1]):
        print key, value
        count += 1
        if count == 10:
            break
    count = 0
    print '--------worst_10--------'
    for key, value in sorted(weight_dict.items(), key = lambda x: x[1]):
        print key, value
        count += 1
        if count == 10:
            break

if __name__ == '__main__':
    main()
