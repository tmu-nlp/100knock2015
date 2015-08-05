#!/usr/bin/python
# -*- coding:utf-8 -*-



def extr_eval_data(data, section):
    i_st = 0 
    for line in data:
        if line == ": {0}".format(section):
            i_st = data.index(line)
            continue
        if i_st != 0 and line[0] == ":":
            i_end = data.index(line)
            break

    eval_data = data[i_st+1:i_end]

    return eval_data


if __name__ == "__main__":
    data = open("questions-words.txt", "r").readlines()
    data = [d.strip() for d in data]

    eval_data = extr_eval_data(data, "family")
    open("eval_instances.txt", "w").write("\n".join(eval_data))  
