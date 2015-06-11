#!usr/bin/python
#coding:utf-8


if __name__ == "__main__":
    input_file = open("nlp.txt", "r")
    output_file = open("output_50.txt", "w")
    separate_list = [".", ";", ":", "?", "!"]
    for line in input_file:
        sentence = ""
        terms = line.strip().split(" ")
        if len(terms) > 1:
            for i in range(len(terms) - 1):
                sentence = sentence + " " + terms[i]
                if terms[i][-1] in separate_list and \
                    "A" <= terms[i + 1][0] <= "Z":
                    print sentence.lstrip(" ")
                    output_file.write(sentence.lstrip(" ") + "\n")
                    sentence = ""
        if sentence == "":
            print line
            output_file.write(line)
        else:
            print sentence.lstrip(" ") + " " + terms[len(terms) - 1]
            output_file.write(sentence.lstrip(" ") + " " + terms[len(terms) - 1] + "\n")

    input_file.close()
    output_file.close()

